from django.db.models import F, ExpressionWrapper, DecimalField
from decimal import Decimal


def calculate_summary(trades):
    """
    trades: queryset of JournalEntry (already filtered to user)
    """

    total = trades.count()
    if total == 0:
        return {
            "total_trades": 0,
            "win_rate": 0,
            "avg_profit": 0,
            "avg_loss": 0,
            "profit_factor": 0,
            "sharpe_ratio": 0,
            "max_drawdown": 0,
            "equity_curve": []
        }

    # Annotate with per-trade PnL
    trades = trades.annotate(
        pnl=ExpressionWrapper(
            (F("exit_price") - F("entry_price")) * F("quantity"),
            output_field=DecimalField(max_digits=15, decimal_places=2),
        )
    )

    pnls = list(trades.values_list("pnl", "trade_date"))

    # Wins & losses
    wins = [p for p, _ in pnls if p > 0]
    losses = [p for p, _ in pnls if p < 0]

    win_rate = len(wins) / total if total else 0
    avg_profit = sum(wins) / len(wins) if wins else Decimal("0")
    avg_loss = sum(losses) / len(losses) if losses else Decimal("0")

    total_profit = sum(wins) if wins else Decimal("0")
    total_loss = abs(sum(losses)) if losses else Decimal("0")
    profit_factor = total_profit / total_loss if total_loss > 0 else 0

    # Equity curve (start at 0, cumulative PnL)
    balance = Decimal("0")
    equity_curve = []
    for pnl, date in sorted(pnls, key=lambda x: x[1]):
        balance += pnl or Decimal("0")
        equity_curve.append({"date": date.date(), "balance": float(balance)})

    # Sharpe ratio (mean / std dev of PnL per trade)
    if len(pnls) > 1:
        pnl_values = [float(p or 0) for p, _ in pnls]
        mean_pnl = sum(pnl_values) / len(pnl_values)
        variance = sum((x - mean_pnl) ** 2 for x in pnl_values) / (len(pnl_values) - 1)
        stddev = variance**0.5
        sharpe = mean_pnl / stddev if stddev > 0 else 0
    else:
        sharpe = 0

    # Max drawdown (as % from peak)
    max_balance = Decimal("0")
    max_drawdown = Decimal("0")
    for point in equity_curve:
        bal = Decimal(point["balance"])
        if bal > max_balance:
            max_balance = bal
        drawdown = (bal - max_balance) / max_balance * 100 if max_balance > 0 else 0
        if drawdown < max_drawdown:
            max_drawdown = drawdown

    return {
        "total_trades": total,
        "win_rate": round(win_rate, 2),
        "avg_profit": float(round(avg_profit, 2)),
        "avg_loss": float(round(avg_loss, 2)),
        "profit_factor": float(round(profit_factor, 2)),
        "sharpe_ratio": round(sharpe, 2),
        "max_drawdown": float(round(max_drawdown, 2)),
        "equity_curve": equity_curve,
    }

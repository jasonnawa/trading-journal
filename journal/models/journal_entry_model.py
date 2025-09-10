from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .tag_model import Tag
from .strategy_model import Strategy
from .ticker_model import Ticker

class JournalEntry(models.Model):
    class TradeStatus(models.TextChoices):
        OPEN = "OPEN", "Open"
        CLOSED = "CLOSED", "Closed"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="journal" )
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    trade_date = models.DateTimeField(default=timezone.now) # default to now if not provided
    quantity = models.BigIntegerField()
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, choices=TradeStatus.choices, default=TradeStatus.OPEN)
    notes = models.TextField(null=True, blank=True)

    @property
    def profit(self): 
        if self.exit_price is not None: 
            return (self.exit_price - self.entry_price) * self.quantity
        return None
    
    @property
    def pnl_percentage(self): 
        if self.exit_price is not None:
            return round(((self.exit_price - self.entry_price)/self.entry_price)  * 100, 2)
        return None
    
    def __str__(self):
        return f"{self.ticker.symbol} - {self.quantity} shares"
    
    class Meta: 
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["ticker"]),
            models.Index(fields=["trade_date"]),
            models.Index(fields=["status"])
        ]
        ordering = ["-trade_date"]
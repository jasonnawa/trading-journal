from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ticker(models.Model):
    symbol =  models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)

class Strategy(models.Model):
    title =  models.CharField(max_length=255, unique=True, db_index=True)
    description = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

class JournalEntry(models.Model):
    class TradeStatus(models.TextChoices):
        OPEN = "OPEN", "Open"
        CLOSED = "CLOSED", "Closed"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
    class Meta: 
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["ticker"]),
            models.Index(fields=["trade_date"]),
            models.Index(fields=["status"])
        ]
        ordering = ["-trade_date"]
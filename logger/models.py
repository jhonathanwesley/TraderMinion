from django.db import models


class Trade(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('PENDING', 'Pending'),
    ]

    TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    CATEGORY_CHOICES = [
        ('CRYPTO', 'Crypto'),
        ('STOCKS', 'Stocks'),
        ('FOREX', 'Forex'),
        ('DERIVATIVES', 'Derivatives'),
    ]

    asset = models.CharField(max_length=100)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    quantity = models.DecimalField(max_digits=18, decimal_places=8)
    entry_price = models.DecimalField(max_digits=18, decimal_places=8)
    exit_price = models.DecimalField(max_digits=18, decimal_places=8, null=True, blank=True)
    stop_loss = models.DecimalField(max_digits=18, decimal_places=8, null=True, blank=True)
    take_profit = models.DecimalField(max_digits=18, decimal_places=8, null=True, blank=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='PENDING')
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)

    class Meta:
        ordering = ['-opened_at']

    def __str__(self):
        return f"{self.asset} - {self.type} ({self.status})"

    @property
    def profit_loss(self):
        if self.exit_price and self.status == 'CLOSED':
            if self.type == 'BUY':
                return float((self.exit_price - self.entry_price) * self.quantity)
            else:
                return float((self.entry_price - self.exit_price) * self.quantity)
        return None

    @property
    def profit_loss_percentage(self):
        if self.exit_price and self.status == 'CLOSED':
            if self.type == 'BUY':
                return float(((self.exit_price - self.entry_price) / self.entry_price) * 100)
            else:
                return float(((self.entry_price - self.exit_price) / self.entry_price) * 100)
        return None

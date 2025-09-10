from django.db import models

class Ticker(models.Model):
    symbol =  models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.symbol
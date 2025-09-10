from django.db import models

class Strategy(models.Model):
    title =  models.CharField(max_length=255, unique=True, db_index=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
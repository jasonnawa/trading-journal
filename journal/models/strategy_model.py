from django.db import models
from django.contrib.auth.models import User
class Strategy(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title =  models.CharField(max_length=255, unique=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
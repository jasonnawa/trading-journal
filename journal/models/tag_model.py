from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.name
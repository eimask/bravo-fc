from django.db import models

# Create your models here.
class Team(models.Model):
    code = models.CharField(max_length=24)
    name = models.CharField(max_length=192)
    is_active = models.BooleanField(default=True)

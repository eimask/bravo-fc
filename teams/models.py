from django.db import models


# Create your models here.
class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=24)
    name = models.CharField(max_length=192)
    isactive = models.BooleanField(default=True)

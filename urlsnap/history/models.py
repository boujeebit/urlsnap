from django.db import models

# Create your models here.
class History(models.Model):
    url = models.CharField(max_length=300,null=True)
    filename = models.CharField(max_length=50,null=True)

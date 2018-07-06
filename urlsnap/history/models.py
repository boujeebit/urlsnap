from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class History(models.Model):
    url = models.CharField(max_length=300,null=True)
    filename = models.CharField(max_length=50,null=True)
    querytime = models.DateTimeField(null=True)

    user = models.ForeignKey(User, default=None, null=True, related_name="user", on_delete=models.SET_NULL)

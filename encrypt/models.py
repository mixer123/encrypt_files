from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Upload(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='User')
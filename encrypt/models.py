from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Upload(models.Model):
    file = models.FileField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
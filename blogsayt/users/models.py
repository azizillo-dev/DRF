from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUSer(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'




from django.contrib.auth.models import AbstractUser
from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice


class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class UserTOTPDevice(TOTPDevice):
    class Meta:
        proxy = True

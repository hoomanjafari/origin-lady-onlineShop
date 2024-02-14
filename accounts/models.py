from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from accounts.managers import MyUserManager


class MyUser(AbstractUser):
    mobile = models.PositiveIntegerField(
        unique=True,
    )

    username = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True
    )

    fullname = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True
    )

    otp = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    otp_created_time = models.DateTimeField(auto_now=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    backend = 'accounts.authentication.MobileAuthentication'

    def __str__(self):
        return f'{self.mobile}'



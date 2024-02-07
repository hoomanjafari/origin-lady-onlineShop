from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from accounts.managers import MyUserManager


class MyUser(AbstractUser):
    mobile = PhoneNumberField(
        region='IR',
        unique=True,
    )

    username = models.CharField(
        max_length=30,
        unique=True,
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

    opt = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    opt_created_time = models.DateTimeField(auto_now=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    backend = 'accounts.authentication.MobileAuthentication'

    def __str__(self):
        return f'{self.mobile}'



from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25, default=None)
    mobile = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    objects = UserManager()

    def __str__(self):
        return self.mobile


    @property
    def is_staff(self):
        return self.is_admin

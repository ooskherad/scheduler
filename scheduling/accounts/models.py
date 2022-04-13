from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25, default=None, null=True)
    mobile = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_image = models.ImageField(default='default.jpeg')

    USERNAME_FIELD = 'mobile'
    objects = UserManager()

    def __str__(self):
        return self.mobile

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    mobile = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} -> {self.mobile} -> {self.created_at}'

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.core.validators import RegexValidator
phone_validator = RegexValidator(r"^[7-9]{1}[0-9]{9}$", "Exactly 10 digits are required")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(max_length=16, validators=[phone_validator], unique=True)
    full_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = ['full_name']
    objects = CustomUserManager()
    def __str__(self):
        return self.mobile
    
class Notice(models.Model):
    title = models.CharField(max_length=80,unique=True)
    description = models.CharField(max_length=255,unique=True)
    
   
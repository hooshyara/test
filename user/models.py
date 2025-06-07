from django.db import models
from .usermanager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from company.models import MainCompany

class User(AbstractUser):
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True)
    fullName = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    personal_code = models.CharField(max_length=100,null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    backend = 'user.backend.PhoneBackend'

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from common.constants import *


class BfrUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True, max_length=30)

    name = models.TextField(max_length=SHORT_TEXT_MAX_LENGTH, blank=False, null=False)
    surname = models.TextField(max_length=SHORT_TEXT_MAX_LENGTH, blank=False, null=False)
    otchestvo = models.TextField(max_length=SHORT_TEXT_MAX_LENGTH, blank=True, null=True)
    telephone = models.CharField(max_length=SHORT_TEXT_MAX_LENGTH, blank=True, null=True)
    is_staff = models.BooleanField(default=False, verbose_name='Административные полномочия')
    is_active = models.BooleanField(default=True, verbose_name='Пользователю разрешен доступ в АРСП')
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь АРСП'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize()
        if self.surname:
            self.surname = self.surname.capitalize()
        if self.otchestvo:
            self.otchestvo = self.otchestvo.capitalize()
        super(BfrUser, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        Returns user's full name with spaces
        """
        if self.otchestvo:
            full_name = '{} {} {}'.format(self.surname, self.name, self.otchestvo)
        else:
            full_name = '{} {}'.format(self.surname, self.name)
        return full_name.strip()

    def get_name_otchestvo(self):
        """
        Returns user's name and otchestvo
        """
        name = '{} {}'.format(self.name, self.otchestvo)
        if self.otchestvo:
            name = '{} {}'.format(self.name, self.otchestvo)
        else:
            name = '{}'.format(self.name)
        return name.strip()

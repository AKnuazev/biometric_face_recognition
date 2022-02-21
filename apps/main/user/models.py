from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from common.constants import *
from recognizer.Recognizer import RecognizationService


class BfrSystem(models.Model):
    emergency_mode = models.BooleanField(default=False, verbose_name='Аварийный режим')

    class Meta:
        verbose_name = 'Система BFR'

    def delete(self, *args, **kwargs):
        raise Exception('Нельзя удалить систему!')

    def save(self, *args, **kwargs):
        if BfrSystem.objects.exists() and not self.pk:
            raise ValidationError('Может быть только одна система!')
        super(BfrSystem, self).save(*args, **kwargs)


class BfrDoor(models.Model):
    code = models.IntegerField(blank=False, null=False, verbose_name='Код двери')
    name = models.CharField(max_length=SHORT_TEXT_MAX_LENGTH, blank=False, null=False, verbose_name='Название двери')

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'

    def __str__(self):
        return 'Дверь {}'.format(self.code)


class BfrUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30, verbose_name='Логин')
    email = models.EmailField(unique=True, max_length=30, verbose_name='Электронная почта')

    name = models.TextField(max_length=SHORT_TEXT_MAX_LENGTH, blank=False, null=False, verbose_name='Имя')
    surname = models.TextField(max_length=SHORT_TEXT_MAX_LENGTH, blank=False, null=False, verbose_name='Фамилия')
    otchestvo = models.TextField(max_length=SHORT_TEXT_MAX_LENGTH, blank=True, null=True, verbose_name='Отчество')
    telephone = models.CharField(max_length=SHORT_TEXT_MAX_LENGTH, blank=True, null=True, verbose_name='Номер телефона')
    acl = models.ManyToManyField(BfrDoor, verbose_name='ACL')
    is_staff = models.BooleanField(default=False, verbose_name='Работник')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_superuser = models.BooleanField(default=False)

    last_indoor = models.ForeignKey(BfrDoor, null=True, blank=True, related_name='users_indoor_list',
                                    verbose_name='Последняя входная дверь', on_delete=models.CASCADE)
    last_outdoor = models.ForeignKey(BfrDoor, null=True, blank=True, related_name='users_outdoor_list',
                                     verbose_name='Последняя выходная дверь', on_delete=models.CASCADE)
    indoor_time = models.DateTimeField(null=True, blank=True, verbose_name='Время входа')
    outdoor_time = models.DateTimeField(null=True, blank=True, verbose_name='Время выхода')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь BFR'
        verbose_name_plural = 'Пользователи BFR'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize()
        if self.surname:
            self.surname = self.surname.capitalize()
        if self.otchestvo:
            self.otchestvo = self.otchestvo.capitalize()

        if not self.pk and not self.is_superuser:
            id = BfrUser.objects.last().pk
            RecognizationService.save_current_image(user_id=id + 1)
            RecognizationService.face_train()

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

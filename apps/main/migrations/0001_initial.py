# Generated by Django 3.2.10 on 2022-02-21 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BfrDoor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Код двери')),
                ('name', models.CharField(max_length=64, verbose_name='Название двери')),
            ],
            options={
                'verbose_name': 'Дверь',
                'verbose_name_plural': 'Двери',
            },
        ),
        migrations.CreateModel(
            name='BfrSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_mode', models.BooleanField(default=False, verbose_name='Аварийный режим')),
            ],
            options={
                'verbose_name': 'Система BFR',
            },
        ),
        migrations.CreateModel(
            name='BfrUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Логин')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Электронная почта')),
                ('name', models.TextField(max_length=64, verbose_name='Имя')),
                ('surname', models.TextField(max_length=64, verbose_name='Фамилия')),
                ('otchestvo', models.TextField(blank=True, max_length=64, null=True, verbose_name='Отчество')),
                ('telephone', models.CharField(blank=True, max_length=64, null=True, verbose_name='Номер телефона')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Работник')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_superuser', models.BooleanField(default=False)),
                ('indoor_time', models.DateTimeField(blank=True, null=True, verbose_name='Время входа')),
                ('outdoor_time', models.DateTimeField(blank=True, null=True, verbose_name='Время выхода')),
                ('acl', models.ManyToManyField(to='main.BfrDoor', verbose_name='ACL')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('last_indoor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_indoor_list', to='main.bfrdoor', verbose_name='Последняя входная дверь')),
                ('last_outdoor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_outdoor_list', to='main.bfrdoor', verbose_name='Последняя выходная дверь')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь BFR',
                'verbose_name_plural': 'Пользователи BFR',
            },
        ),
    ]

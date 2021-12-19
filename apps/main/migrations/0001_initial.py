# Generated by Django 4.0 on 2021-12-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BfrUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('name', models.TextField(max_length=64)),
                ('surname', models.TextField(max_length=64)),
                ('otchestvo', models.TextField(blank=True, max_length=64, null=True)),
                ('telephone', models.CharField(blank=True, max_length=64, null=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Административные полномочия')),
                ('is_active', models.BooleanField(default=True, verbose_name='Пользователю разрешен доступ в АРСП')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь АРСП',
            },
        ),
    ]
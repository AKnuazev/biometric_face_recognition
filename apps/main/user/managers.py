from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    # use_in_migrations = True

    def _create_user(self, username, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not username:
            raise ValueError('login должен быть указан')
        user = self.model(username=username, **extra_fields)
        if not password:
            password = 123
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, **extra_fields)

    def create_superuser(self, username, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, **extra_fields)

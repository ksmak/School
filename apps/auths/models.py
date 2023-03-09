# Django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    """Custom user manager."""
    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        patronymic: str
    ) -> 'CustomUser':
        if not email:
            raise ValueError("Email is null.")

        if not password:
            raise ValueError("Password is null.")

        if not first_name:
            raise ValueError("First name is null.")

        if not last_name:
            raise ValueError("Last name is null.")

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str

    ) -> 'CustomUser':
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """Custom user model."""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=150
    )
    patronymic = models.CharField(
        verbose_name='patronymic',
        max_length=150,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='is active',
        default=True
    )
    is_superuser = models.BooleanField(
        verbose_name='is superuser',
        default=False
    )
    create_date = models.DateTimeField(
        verbose_name='created date',
        auto_now_add=True
    )
    change_date = models.DateTimeField(
        verbose_name="changed date",
        auto_now=True
    )

    @property
    def is_staff(self):
        return self.is_superuser

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('create_date', )

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

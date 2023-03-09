# Django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# Project
from abstracts.utils import get_activation_code


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
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """Custom user model."""
    ACTIVATION_CODE_SIZE = 12
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
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='is staff',
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name='is superuser',
        default=False
    )
    activation_code = models.CharField(
        verbose_name='activate code',
        max_length=ACTIVATION_CODE_SIZE
    )
    create_date = models.DateTimeField(
        verbose_name='created date',
        auto_now_add=True
    )
    change_date = models.DateTimeField(
        verbose_name="changed date",
        auto_now=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('create_date', )

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def save(self, *args, **kwargs) -> None:
        self.activation_code = \
            get_activation_code(self.ACTIVATION_CODE_SIZE)
        super().save(*args, **kwargs)

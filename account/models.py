from django.db import models

from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser

from .choices import USER_ROLE_CHOICES

from django.core.validators import MinValueValidator, MaxValueValidator

class UserManager(BaseUserManager):
    def create_user(self, number, password=None, **extra_fields):
        if not number:
            raise ValueError("Users must have a phone number")

        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(number, password, **extra_fields)


class User(AbstractUser):
    username = None

    number = models.CharField(
        max_length=11,
        verbose_name="number",
        help_text="Enter your number",
        unique=True,
    )

    email = models.EmailField(
        verbose_name="email address",
        help_text="Enter your email",
        blank=True,
        null=True,
        unique=True,
    )

    # is_private = models.BooleanField(
    #     default=False,
    #     verbose_name="private account",
    # )

    is_active = models.BooleanField(
        default=True,
        verbose_name="active",
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    last_update = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )

    USERNAME_FIELD = "number"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    class Meta:
        verbose_name = "1. user"

    def __str__(self):
        return self.number


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name="first name",
        help_text="Enter your first name",
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="last name",
        help_text="Enter your last name",
    )

    address = models.TextField(
        max_length=100,
        verbose_name="address",
        help_text="Enter your address",
    )

    role =models.CharField(
        choices=USER_ROLE_CHOICES
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )



class Reviews(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="title",
    )

    rating= models.FloatField(
        verbose_name="rating",
        help_text="Enter your rating",
    validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ]
    )

    text = models.TextField(
        verbose_name="text",
        help_text="Enter your text",
        max_length=1024,
    )

    vehicleID = models.CharField(
        max_length=100,
        verbose_name="the vehicle this review belongs to",
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )



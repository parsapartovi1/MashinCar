from django.contrib.auth.models import User
from django.db import models

from .choices import (
    MODEL_CHOICES,
    CONDITION_STATUS,
    DAMAGE_STATUS,
    REPAIR_STATUS,
    VEHICLE_TYPE,
    PART_CATEGORY
)

from payment.models import Discount

class Country(models.Model):
    country=models.CharField(
        verbose_name="country",
        max_length=200,
    )

    order_of=models.CharField(
        verbose_name="order_of",
        max_length=200,
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )


class Brand(models.Model):
    brand_name=models.CharField(
        verbose_name="brand name",
    )

    logo=models.ImageField(
        verbose_name="logo",

    )

    country=models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )

    founded=models.DateField(
        verbose_name="founded year",
    )

    description=models.TextField(
        verbose_name="description",
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )


class Condition(models.Model):
    condition=models.CharField(
        verbose_name="condition",
        choices=CONDITION_STATUS,
    )

    damage=models.CharField(
        verbose_name="damage",
        choices=DAMAGE_STATUS,
    )

    repair=models.CharField(
        verbose_name="repair",
        choices=REPAIR_STATUS,
    )

    is_repairable=models.BooleanField(
        verbose_name="is_repairable",
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )


class Image(models.Model):
    image=models.ImageField(
        verbose_name="Image",
    )

class VehicleType(models.Model):
    vehicle_type=models.CharField(
        choices=VEHICLE_TYPE,
    )

class Vehicle(models.Model):
    name = models.CharField(
        verbose_name="vehicle name",
        max_length=200,
        null=False,
        blank=False,
    )

    model=models.CharField(
        verbose_name="model",
        choices=MODEL_CHOICES,
    )

    year = models.CharField(
        verbose_name="year",
        max_length=200,
        null=False,
        blank=False,
    )

    description=models.CharField(
        verbose_name="description",
    )

    price=models.CharField(
        verbose_name="price",
    )

    Discount=models.OneToOneField(
        Discount,
        verbose_name="Discount ID",
        on_delete=models.CASCADE,
    )

    Image=models.ForeignKey(
        Image,
        verbose_name="Image",
        on_delete=models.CASCADE,
    )

    vehicle_type=models.OneToOneField(
        VehicleType,
        verbose_name="Vehicle Type",
        on_delete=models.CASCADE,
    )

    brand=models.OneToOneField(
        Brand,
        verbose_name="Brand",
        on_delete=models.CASCADE,
    )

    condition=models.OneToOneField(
        Condition,
        verbose_name="Condition",
        on_delete=models.CASCADE,
    )

    user=models.OneToOneField(
        User,
        verbose_name="User",
        on_delete=models.SET_NULL,
    )

    country=models.OneToOneField(
        Country,
        verbose_name="Country",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        verbose_name="creation date",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="last update",
        auto_now=True,
    )

class Part(models.Model):
    part=models.CharField(
        verbose_name="part name",
        max_length=200,
    )

    part_category=models.CharField(
        verbose_name="part category",
        choices=PART_CATEGORY
    )

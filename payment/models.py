from django.db import models


class Discount(models.Model):
    amount = models.IntegerField(
        verbose_name="Discount Percent",
        help_text="Enter discount amount"
    )

    duration = models.DateTimeField(
        verbose_name="Valid Until",
        help_text="Discount validity duration"
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Create Date"
    )

    last_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Update"
    )

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return f"{self.amount}% until {self.duration}"


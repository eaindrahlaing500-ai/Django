
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    max_allowed_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock_quantity = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    is_promotional = models.BooleanField(default=False)

    status = models.CharField(max_length=50)
    warehouse_country = models.CharField(max_length=50)

    total_sold = models.IntegerField(default=0)

    total_revenue = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return self.name

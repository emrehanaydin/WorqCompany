from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Merchant(models.Model):
    id = models.AutoField(primary_key=True)
    merchant_name = models.CharField(max_length=255, null=False)
    followers = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    score = models.FloatField(default=0.0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merchant_url = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.merchant_name}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="")
    image_url = models.URLField(null=True)
    brand = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name}-{self.price}"

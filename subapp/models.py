from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()
    ratings = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name

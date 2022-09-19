from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Place(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    type = models.CharField(max_length=50)
    picture = models.TextField()

    class Meta:
        ordering = ['created_at']

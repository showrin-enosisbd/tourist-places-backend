from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from account.models import User


class Place(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    type = models.CharField(max_length=50)
    picture = models.TextField()
    creator = models.ForeignKey(
        User, related_name='places', on_delete=models.CASCADE, null=True, blank=True, default=0)

    class Meta:
        ordering = ['created_at']

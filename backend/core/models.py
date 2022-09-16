from django.db import models


class User(models.Model):
    name = models.CharField(blank=True, default='')
    email = models.EmailField()
    password = models.CharField()

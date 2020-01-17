from django.db import models
from django.core import validators
# Create your models here.
class Members(models.Model):
    objects = models.Manager()
    firstName = models.CharField(max_length=254, unique=False)
    lastName = models.CharField(max_length=254, unique=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    verifyPassword = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
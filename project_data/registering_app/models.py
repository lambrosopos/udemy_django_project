from django.db import models
from django.core import validators
from django.contrib.auth.models import User
# Create your models here.
        
class UserProfileInfo(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Addtional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username

class Members(models.Model):
    objects = models.Manager()
    firstName = models.CharField(max_length=254, unique=False)
    lastName = models.CharField(max_length=254, unique=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
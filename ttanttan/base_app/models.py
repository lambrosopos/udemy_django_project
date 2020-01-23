from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional 
    portfolioSite = models.URLField(blank=True)
    profilePic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username
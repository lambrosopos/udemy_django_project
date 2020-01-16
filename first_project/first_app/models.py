from django.db import models

# Create your models here.
class Topic(models.Model):
    objects = models.Manager()
    top_name = models.CharField(max_length = 264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    objects = models.Manager()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    objects = models.Manager()
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    objects = models.Manager()
    firstName = models.CharField(max_length=20, unique=False)
    lastName = models.CharField(max_length=20, unique=False)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.lastName



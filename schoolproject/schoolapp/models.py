from django.db import models
from django.urls import reverse


# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Profiles(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    age = models.IntegerField()
    phone = models.TextField()
    course = models.TextField(max_length=250)
    gender = models.TextField()
    mail_id = models.EmailField()
    DOB = models.DateField(auto_now_add=True)
    department = models.TextField(max_length=140, default='SOME STRING')

    def __str__(self):
        return self.name

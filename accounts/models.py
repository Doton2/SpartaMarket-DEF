from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=20)
    Nick_name = models.CharField(max_length=20)
    birthday = models.DateField()

    gender_choice = [
        ('M','male' )
        ,('F','female')
    ]
    gender = models.CharField(max_length=1, choices=gender_choice, blank= True)
    content = models.TextField(blank=True)
    
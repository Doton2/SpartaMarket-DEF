from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)

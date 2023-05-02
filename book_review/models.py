from django.db import models
from django.contrib.auth import User


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=300, blank=False, unique=True)
    author = models.CharField(max_length=300, blank=False, unique=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    blurb = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    approved = models.BooleanField(default=False)
    like_count = models.ManyToManyField(User, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
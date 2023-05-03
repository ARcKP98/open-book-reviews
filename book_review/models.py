from django.db import models
from django.contrib.auth import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=300, blank=False, unique=True)
    author = models.CharField(max_length=300, blank=False, unique=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='book_genre')
    blurb = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    approved = models.BooleanField(default=False)
    like_count = models.ManyToManyField(User, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_contributor')
    image = CloudinaryField('image', default='Placeholder')

    class Meta:
        ordering = ['-created_on']

        def number_of_likes(self):
            return self.like_count.count()

        def __str__(self):
            return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

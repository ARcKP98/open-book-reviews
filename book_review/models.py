from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import reverse


# Create your models here.

class Genre(models.Model):
    '''
    Genre Model.
    '''
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Book(models.Model):
    '''
    Book model.
    '''
    name = models.CharField(max_length=300, unique=True)
    author = models.CharField(max_length=300, blank=False, null=False,
                              unique=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT,
                              related_name='book_genre')
    blurb = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    approved = models.BooleanField(default=False)
    read_count = models.ManyToManyField(User, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='book_contributor')
    image = CloudinaryField('image', default='Placeholder', blank=True)

    '''
    Returns the number of people who have read the book.
    '''
    def number_of_read(self):
        return self.read_count.count()

    def __str__(self):
        return self.name


class Review(models.Model):
    '''
    Review Model.
    '''
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='review_by')
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE,
                                  related_name='review_for')
    details = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # Reviews are ordered in a descending order(most to least recent).
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.details} by {self.username}"

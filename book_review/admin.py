from django.contrib import admin
from .models import Genre, Book, Review


# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_filter = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'author']
    list_display = ['name', 'author', 'genre', 'blurb']
    list_filter = ['approved', 'genre']
    actions = ['book_approved']

    def book_approved(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['username', 'book_name']
    list_display = ['username', 'book_name', 'details', 'created_on']
    list_filter = ['approved']
    actions = ['review_approved']

    def review_approved(self, request, queryset):
        queryset.update(approved=True)

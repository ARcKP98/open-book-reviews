from django.contrib import admin
from .models import Genre, Book, Review

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_filter = ['name']



admin.site.register(Book)
admin.site.register(Review)

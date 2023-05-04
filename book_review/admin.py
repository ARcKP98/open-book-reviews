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
    list_display = ['name', 'author', 'genre', 'approved']
    list_filter = ['approved', 'genre']
    actions = ['book_approved']

    def book_approved(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Review)

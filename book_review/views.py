from django.shortcuts import render
from django.views import generic
from .models import Book, Genre


# Create your views here.
# class BookList(generic.ListView):
#     model = Book
#     queryset = Book.objects.filter(approved=True).order_by('?')
#     template_name = 'index.html'
#     paginate_by = 6


class GenreList(generic.ListView):
    model = Genre
    template_name = 'index.html'
    queryset = Genre.objects.order_by('name')
    paginate_by = 6


class ViewGenreTitles(generic.ListView):
    template_name = 'genre.html'
    context_object_name = 'genre_items'

    def get_queryset(self):
        content = {
            'genre': self.kwargs['genre'],
            'books': Book.objects.filter(genre__slug=self.kwargs['genre']).filter(approved=True)
        }
        return content

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book, Genre


# Create your views here.

class GenreList(generic.ListView):
    model = Genre
    template_name = 'index.html'
    queryset = Genre.objects.order_by('name')
    paginate_by = 6


class ViewGenreTitles(generic.ListView):
    template_name = 'books.html'
    context_object_name = 'genre_items'

    def get_queryset(self):
        content = {
            'genre': self.kwargs['genre'],
            'books': Book.objects.filter
            (genre__slug=self.kwargs['genre']).filter(approved=True)
        }
        return content


class BookInfo(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)
        like = False
        if book.like_count.filter(id=self.request.user.id).exists():
            like = True
        return render(
            request,
            'book-info.html',
            {
                'book': book,
                'like': like,
            }
        )

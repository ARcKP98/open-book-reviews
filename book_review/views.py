from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book, Genre, Review
from .forms import ReviewForm


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
        review = book.review_for.filter(approved=True)

        return render(
            request,
            "book-info.html",
            {
                "book": book,
                "reviews": review,
                "reviewed": False,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.review_for.filter(approved=True)

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.username = request.user
            review = review_form.save(commit=False)
            review.book_name = book
            review.save()
        else:
            review_form = ReviewForm()
        return render(
            request,
            "book-info.html",
            {
                "book": book,
                "reviews": reviews,
                "reviewed": True,
                "review_form": review_form
            },
        )
    
   
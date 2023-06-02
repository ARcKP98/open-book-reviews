from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Book, Genre, Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect


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
        liked = False
        if book.like_count.filter(id=request.user.id).exists():
            liked = True
        return render(
            request,
            "book-info.html",
            {
                "book": book,
                "reviews": review,
                "reviewed": False,
                "liked": liked,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.review_for.filter(approved=True)
        liked = False
        if book.like_count.filter(id=request.user.id).exists():
            liked = True

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
                "liked": liked,
                "review_form": review_form
            },
        )


class LikeBook(View):
    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        if book.like_count.filter(id=request.user.id).exists():
            book.like_count.remove(request.user)
        else:
            book.like_count.add(request.user)
        
        return HttpResponseRedirect(reverse('book-info', args=[slug]))

   
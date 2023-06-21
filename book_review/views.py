from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from .models import Book, Genre, Review
from .forms import ReviewForm, BookForm
from django.http import HttpResponseRedirect


# Create your views here.

class GenreList(generic.ListView):
    '''
    Displays all the genres on the home page.
    '''
    model = Genre
    template_name = 'index.html'
    queryset = Genre.objects.order_by('name')
    paginate_by = 6


class ViewGenreTitles(generic.ListView):
    '''
    Displays all the books that are associated with the genre.
    Only the books that are approved by the admin will be displayed.
    '''
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
    '''
    Displays all the information associated with the book. The
    user can then add a review to the book using the form that is provided
    and can select whether they have read the book or not.
    '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)
        review = book.review_for.filter(approved=True)
        read = False
        if book.read_count.filter(id=request.user.id).exists():
            read = True
        return render(
            request,
            "book-info.html",
            {
                "book": book,
                "reviews": review,
                "reviewed": False,
                "read": read,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.review_for.filter(approved=True)
        read = False
        if book.read_count.filter(id=request.user.id).exists():
            read = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.username = request.user
            review = review_form.save(commit=False)
            review.book_name = book
            review.save()
            messages.success(
                self.request,
                'Review received! It will now get checked by the Admin.'
                )
        else:
            review_form = ReviewForm()
        return render(
            request,
            "book-info.html",
            {
                "book": book,
                "reviews": reviews,
                "reviewed": True,
                "read": read,
                "review_form": ReviewForm()
            },
        )


class AddBook(LoginRequiredMixin, View):
    '''
    Allows logged in users to fill out a form to
    add a book to the collection. The book is then
    approved/disapproved by the admin.
    '''
    def get(self, request):
        return render(
            request,
            "add-book.html",
            {
                "book_form": BookForm()
            },
        )

    def post(self, request):
        book_form = BookForm(request.POST, request.FILES)

        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.uploaded_by = request.user
            book.slug = slugify('-'.join([book.name, str(book.author)]),
                                allow_unicode=False)
            book.save()
            messages.success(
                self.request,
                'Your book submission was successful.' +
                'It will now be checked by admin.'
                )

        else:
            book_form = BookForm()

        return render(
            request,
            "add-book.html",
            {
                "book_form": BookForm()
            },
        )


class EditReview(UpdateView):
    '''
    Allows users to edit their original review for a book.
    '''
    model = Review
    fields = ('details',)
    template_name = 'edit-review.html'

    def get_success_url(self):
        messages.info(self.request, 'Your review was updated successfully.')
        return reverse('book-info',
                       kwargs={'slug': self.object.book_name.slug})


class DeleteReview(DeleteView):
    '''
    Allows users to delete their original review for a book.
    '''
    model = Review
    template_name = 'delete-review.html'

    def get_success_url(self):
        messages.info(self.request, 'Your review was deleted successfully.')
        return reverse('book-info',
                       kwargs={'slug': self.object.book_name.slug})


class ReadBook(View):
    '''
    Allows users to show whether they have read the book or not.
    '''
    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        if book.read_count.filter(id=request.user.id).exists():
            book.read_count.remove(request.user)
        else:
            book.read_count.add(request.user)

        return HttpResponseRedirect(reverse('book-info', args=[slug]))


class ContactUs(TemplateView):
    '''
    Contact form to connect with the admin.
    '''
    template_name = 'contact-form.html'

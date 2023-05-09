from django.shortcuts import render
from django.views import generic
from .models import Book


# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(approved=True).order_by('?')
    template_name = 'index.html'
    paginate_by = 6

from .models import Review, Book
from django import forms


class ReviewForm(forms.ModelForm):
    '''
    Review form.
    '''
    class Meta:
        model = Review
        fields = ('details',)


class BookForm(forms.ModelForm):
    '''
    Add book form.
    '''
    class Meta:
        model = Book
        fields = ('name', 'author', 'genre', 'blurb', 'image')

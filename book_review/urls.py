from . import views
from django.urls import path

urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path("genre/<genre>/", views.ViewGenreTitles.as_view(), name="books"),
    path('add-book/', views.AddBook.as_view(), name='add-book'),
    path('like/<slug:slug>', views.LikeBook.as_view(), name="book_liked"),
    path('edit-book/<int:pk>', views.EditBook.as_view(), name="edit-review"),
    path('<slug:slug>/', views.BookInfo.as_view(), name='book-info'),
]

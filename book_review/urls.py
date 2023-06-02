from . import views
from django.urls import path

urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path("genre/<genre>/", views.ViewGenreTitles.as_view(), name="books"),
    path('<slug:slug>/', views.BookInfo.as_view(), name='book-info'),
    path('like/<slug:slug>', views.LikeBook.as_view(), name="book_liked"),
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path("genre/<genre>/", views.ViewGenreTitles.as_view(), name="books"),
    path('add-book/', views.AddBook.as_view(), name='add-book'),
    path('like/<slug:slug>', views.LikeBook.as_view(), name="book_liked"),
    path('edit-book/<int:pk>', views.EditReview.as_view(), name="edit-review"),
    path('<int:pk>/delete-review', views.DeleteReview.as_view(), name="delete-review"),
    path('book-info/<slug:slug>/delete-book/', views.DeleteBook.as_view(), name="delete-book"),
    path('book-info/<slug:slug>/', views.BookInfo.as_view(), name='book-info'),
]

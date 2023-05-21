from . import views
from django.urls import path

urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path("genre/<genre>/", views.ViewGenreTitles.as_view(), name="genre"),
    path('<slug:slug>/', views.BookInfo.as_view(), name='book-info'),
]

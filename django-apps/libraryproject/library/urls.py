from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books_view, name='list_books'),
    path('add/', views.add_book_view, name='add_book'), 
]

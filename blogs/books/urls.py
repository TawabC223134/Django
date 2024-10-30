from django.urls import path
from books.views import my_view, BookListView ,My_View,ContactFormView,BookCreateView
from books.views import BookListCreateView
from books.views import MyView
from django.shortcuts import render 


urlpatterns = [
    path("initial/",my_view),
    path('initial_class/',MyView.as_view()),
    path('list/',BookListView.as_view() ,name='list'), # Ensure the name is 'list
    path('initial_class_books/',My_View.as_view()),
    path("contact/add", ContactFormView.as_view()), 
    path("contact_success/", lambda request: render(request, "success/contact_success.html"), name="contact_success"), 
    path('create/',BookCreateView.as_view(), name='create_book'),
    path('books_rest/', BookListCreateView.as_view(),name = 'book_list_create'),
    
]
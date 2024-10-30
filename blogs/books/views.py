#from django
from django.shortcuts import HttpResponse
from django.views import View
from django.urls import reverse_lazy 
from django.views.generic import ListView,FormView,CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#from books
from books.models import Book
from books.forms import ContactFormView,BookForm
from books.serializers import BookSerializer


##Function based
def my_view(request):
    return HttpResponse('Welcome to Django from Function')
### create a file name urls.py

###Class based
class MyView(View):
    def get(self,request):
        return HttpResponse("Welcome Again to Django form Class")
    

class BookListView(ListView):
    model=Book
    template_name = "book_list.html"
    context_object_name = "books"

class My_View(View):
    def get(self,request):
        return HttpResponse("Welcome to Djago from Class")

#import FormView  from django.views.generic 
class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactFormView
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form) -> HttpResponse: 
        return super().form_valid(form)

#import CreateView from django.views.generic
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

#rest_framework API's
class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        data = serializer.data
        return Response(data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
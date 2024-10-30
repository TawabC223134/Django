#from django
from django.shortcuts import HttpResponse,get_object_or_404
from django.views import View
from django.urls import reverse_lazy 
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

#from rest_framework
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import status, permissions 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

#from books
from books.models import Book # importing from Book Model
from books.forms import ContactFormView, BookForm
from books.serializers import BookSerializer

# importing from Author
from rest_framework import generics
from books.models import Author
from books.serializers import AuthorSerializer

# importing from Publisher
from .models import Publisher
from .serializers import PublisherSerializer

## Function based
def my_view(request):
    return HttpResponse('Welcome to Django from Function')
### create a file name urls.py

### Class based
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        data = serializer.data
        return Response(data, status = status.HTTP_200_OK)
    
    #def post(self, request, pk):
        #isinstance = Book.objects.get(id=pk) #keyword argument
        #serializer = BookSerializer(isinstance,data = request.data)
        #isinstance = get_object_or_404(Book, pk=pk)
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthorListCreateView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PublisherListCreateView(APIView):
    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookGetUpdateDelete(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    def get(self, request):
        return self.retrieve(request, *args, **kwargs)


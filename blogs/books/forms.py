from django import forms
from django.core.exceptions import ValidationError
from books.models import Book

class ContactFormView(forms.Form):
    name = forms.CharField(max_length=100)  
    email = forms.EmailField() 
    message = forms.CharField(widget=forms.Textarea) 
     
    def clean_email(self): 
        email = self.cleaned_data.get('email') 
         
        if not email.endswith("@example.com"): 
            raise forms.ValidationError("Email must be from example.com domain.") 
        return email
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'description', 'author']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price
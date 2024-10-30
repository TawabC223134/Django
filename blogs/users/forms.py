from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(max_length=200)
    

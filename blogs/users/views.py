# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('list')  # Redirect to homepage or another page

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Logs the user in automatically
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)

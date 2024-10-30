# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('list')  # Redirect to homepage or another page

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Logs the user in automatically
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
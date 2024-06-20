from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def custom_logout_view(request):
    logout(request)
    return redirect("home")

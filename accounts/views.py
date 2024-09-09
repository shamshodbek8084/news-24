from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserRegistrationForm
from .models import User
# Create your views here.


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    def get(self, request):
        form = self.form_class()
        context = {
            "form":form

        }
        return redirect(request, "accounts/signup.html", context)

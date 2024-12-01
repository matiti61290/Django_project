from django.shortcuts import render, redirect
from mediatheque.forms import LoginForm
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'home.html')

class LoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
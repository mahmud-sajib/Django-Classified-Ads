from django.shortcuts import render

# Create your views here.

def signup_view(request):
    return render(request, 'authentication/signup.html')

def login_view(request):
    return render(request, 'authentication/login.html')
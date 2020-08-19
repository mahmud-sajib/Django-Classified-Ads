from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.db.models import Count, Q

# importing messages
from django.contrib import messages

# Model Forms.

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')



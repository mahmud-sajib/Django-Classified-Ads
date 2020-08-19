from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.db.models import Count, Q

# importing messages
from django.contrib import messages

# Model Forms.

# Create your views here.
def profile_dashboard(request):
    return render(request, 'profiles/account-dashboard.html')

def profile_settings(request):
    return render(request, 'profiles/account-setting.html')

def profile_ads(request):
    return render(request, 'profiles/all-ads.html')

def profile_favorite_ads(request):
    return render(request, 'profiles/favourite-ads.html')

def profile_close(request):
    return render(request, 'profiles/account-close.html')




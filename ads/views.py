from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Count
# Model Forms.
from .forms import PostAdsForm
from django.contrib.auth.forms import User
from django.contrib.auth.models import User

# importing messages
from django.contrib import messages

from ads.models import Author
# Create your views here.


# def get_author(user):
#     qs = Author.objects.filter(user=user)
#     if qs.exists():
#         return qs[0]
#     return None

# Post ads view
def post_ads(request):
    if request.method == 'POST':

        length = request.POST.get('length')
        
        title = request.POST.get('title')

        description = request.POST.get('description')

        category = request.POST.get('category')
        
        # c = Category.objects.get_or_create(category_name=category)
        category_check = Category.objects.filter(category_name=category).exists()
        print(category_check)
        
        if category_check:
            c = Category.objects.get(category_name=category)
        else:
            c = Category.objects.create(category_name=category)
        
        # c = Category.objects.create(category_name=category)
        print(f"CATEGORY:{c}")

        price = request.POST.get('price')
        condition = request.POST.get('condition')
        state = request.POST.get('state')
        city = request.POST.get('city')
        brand = request.POST.get('brand')
        phone = request.POST.get('phone')
        video = request.POST.get('video')

        ads = Ads.objects.create(author=request.user.author, title=title, description=description, price=price, category=c, condition=condition, state=state, city=city, brand=brand, phone=phone, video=video)

        print(f"ADS: {ads}")

        for file_num in range(0, int(length)):
            AdsImages.objects.create(
                ads=ads,
                image=request.FILES.get(f'images{file_num}')
            )
        
    return render(request, 'ads/post-ads.html')

# Ads listing view
def ads_listing(request):
    ads_listing = Ads.objects.all()
    category_listing = Category.objects.annotate(total_ads=Count('ads')) 

    context = {
        'ads_listing' : ads_listing,
        'category_listing' : category_listing
    }

    return render(request, 'ads/ads-listing.html', context)

# Ads detail view
def ads_detail(request, pk):
    ads_detail = get_object_or_404(Ads, pk=pk)
    ads_photos = AdsImages.objects.filter(ads=ads_detail)

    context = {
        'ads_detail' : ads_detail,
        'ads_photos' : ads_photos,
    }

    return render(request, 'ads/ads-detail.html', context)

# Ads category archive view
def ads_category_archive(request, slug):
    category = get_object_or_404(Category, slug=slug)
    ads_by_category = Ads.objects.filter(category=category)

    context = {
        'category' : category,
        'ads_by_category' : ads_by_category
    }

    return render(request, 'ads/category-archive.html', context)

# Ads search/filter view
def ads_search(request):

    state = request.GET.get('state')
    category = request.GET.get('category_name')

    ads_search_result = Ads.objects.filter(state=state).filter(category__category_name=category)
    
    context = {
        'ads_search_result':ads_search_result
    }

    return render(request, 'ads/ads-search.html', context)

def ads_delete(request, pk):
    ad = get_object_or_404(Ads, pk=pk)
    ad.delete()
    return redirect("dashboard")










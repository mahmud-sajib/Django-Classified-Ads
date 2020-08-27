from django.shortcuts import render, get_object_or_404
from .models import Ads, Category
from django.db.models import Count
# Create your views here.

def post_ads(request):
    return render(request, 'ads/post-ads.html')

def ads_listing(request):
    ads_listing = Ads.objects.all()
    category_listing = Category.objects.annotate(total_ads=Count('ads')) 

    context = {
        'ads_listing' : ads_listing,
        'category_listing' : category_listing
    }

    return render(request, 'ads/ads-listing.html', context)

def ads_detail(request, pk):
    ads_detail = get_object_or_404(Ads, pk=pk)

    context = {
        'ads_detail' : ads_detail,
    }

    return render(request, 'ads/ads-detail.html', context)


def ads_category_archive(request, slug):
    category = get_object_or_404(Category, slug=slug)
    ads_by_category = Ads.objects.filter(category=category)

    context = {
        'category' : category,
        'ads_by_category' : ads_by_category
    }

    return render(request, 'ads/category-archive.html', context)

def ads_search(request):
    ads_search = Ads.objects.order_by('-date_created')
    ads_category = Category.objects.order_by('-date_created')

    if 'state' in request.GET:
        state = request.GET['state']
        
        print(f"LOCATION {state}")
        
        if state:
            ads_search = ads_search.filter(state__iexact=state)
    
    if 'category_name' in request.GET:
        category_name = request.GET['category_name']
        
        print(f"CAT {category_name}")
        
        if category_name:
            ads_category = Category.objects.filter(category_name__icontains=category_name)

    context = {
        'ads_search' : ads_search,
        'ads_category' : ads_category
    }

    return render(request, 'ads/ads-search.html', context)








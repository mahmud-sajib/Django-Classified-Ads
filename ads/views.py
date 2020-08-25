from django.shortcuts import render, get_object_or_404
from .models import Ads

# Create your views here.

def post_ads(request):
    return render(request, 'ads/post-ads.html')

def ads_listing(request):
    ads_listing = Ads.objects.all()

    context = {
        'ads_listing' : ads_listing,
    }

    return render(request, 'ads/ads-listing.html', context)

def ads_detail(request, pk):
    ads_detail = get_object_or_404(Ads, pk=pk)

    context = {
        'ads_detail' : ads_detail,
    }

    return render(request, 'ads/ads-detail.html', context)




from django.shortcuts import render

# Create your views here.

def post_ads(request):
    return render(request, 'ads/post-ads.html')

def ads_listing(request):
    return render(request, 'ads/ads-listing.html')

def ads_detail(request):
    return render(request, 'ads/ads-detail.html')




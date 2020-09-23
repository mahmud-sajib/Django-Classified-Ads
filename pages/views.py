from django.shortcuts import render, get_object_or_404

from ads.models import Ads, Category, AdsImages

# Model Forms.

# Create your views here.

# Home view
def home(request):
    pk=None
    ads=None
    # Fetch recend ads
    recent_ads = Ads.objects.order_by('date_created')[0:3]
    
    # Fetch featured Ads
    featured_ads = Ads.objects.filter(is_featured=True)

    # p = recent_ads.filter(adsimages__image.url)
    # print(f"Photo: {f_p}")

    

    # print(f"Photo: {f_p}")

    # Fetch search location & category 
    location_search = Ads.objects.values_list('state', flat=True).distinct()
    category_search = Category.objects.values_list('category_name', flat=True).distinct()
    
    # Contexts
    context = {
        'recent_ads' : recent_ads,
        'featured_ads' : featured_ads,
        # 'ads_detail' : ads_detail,
        # 'ads_photos' : ads_photos,
        'location_search' : location_search,
        'category_search' : category_search,
    }

    return render(request, 'pages/index.html', context)

# Faq view
def faq(request):
    return render(request, 'pages/faq.html')

# Contact view
def contact(request):
    return render(request, 'pages/contact.html')



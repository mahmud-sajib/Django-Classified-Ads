from django.shortcuts import render, get_object_or_404

from ads.models import Ads, State, City, Category, AdsImages, AdsTopBanner, AdsRightBanner, AdsBottomBanner

# Model Forms.

# Create your views here.

# Home view
def home(request):
    
    # Fetch recend ads
    recent_ads = Ads.objects.filter(is_active=True).order_by('date_created')[0:3]
    
    # Fetch featured Ads
    featured_ads = Ads.objects.filter(is_featured=True).filter(is_active=True)
    
    # Browse Ads by Category
    category_listing = Category.objects.all()

    # Browse Ads by State
    state_listing = State.objects.all()

    # Fetch Ads Banner
    sidebar_banners = AdsRightBanner.objects.all()
    top_banner = AdsTopBanner.objects.all()
    bottom_banner = AdsBottomBanner.objects.all()

    # Fetch search location & category 
    state_search = State.objects.values_list('state_name', flat=True).distinct().order_by("state_name")
    category_search = Category.objects.values_list('category_name', flat=True).distinct().order_by("category_name")
    
    # Contexts
    context = {
        'recent_ads' : recent_ads,
        'featured_ads' : featured_ads,
        'state_search' : state_search,
        'category_search' : category_search,
        'category_listing' : category_listing,
        'state_listing' : state_listing,
        'sidebar_banners' : sidebar_banners,
        'top_banner' : top_banner,
        'bottom_banner' : bottom_banner,
    }

    return render(request, 'pages/index.html', context)

# Faq view
def faq(request):
    return render(request, 'pages/faq.html')

# Terms of service view
def terms_of_service(request):
    return render(request, 'pages/terms-of-service.html')

# Contact view
def contact(request):
    return render(request, 'pages/contact.html')



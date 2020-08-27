from django.shortcuts import render

from ads.models import Ads, Category

# Model Forms.

# Create your views here.

def home(request):
    recent_ads = Ads.objects.order_by('date_created')[0:3]
    featured_ads = Ads.objects.filter(is_featured=True)
    # view_log = str(featured_ads.query)
    # print(view_log)

    location_search = Ads.objects.values_list('state', flat=True).distinct()
    category_search = Category.objects.values_list('category_name', flat=True).distinct()
    print(location_search)
    print(category_search)
    
    context = {
        'recent_ads' : recent_ads,
        'featured_ads' : featured_ads,
        'location_search' : location_search,
        'category_search' : category_search,
    }

    return render(request, 'pages/index.html', context)

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')



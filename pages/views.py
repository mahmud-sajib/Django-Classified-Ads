from django.shortcuts import render

from ads.models import Ads

# Model Forms.

# Create your views here.

def home(request):
    recent_ads = Ads.objects.order_by('date_created')[0:3]
    featured_ads = Ads.objects.filter(is_featured=True)
    # view_log = str(featured_ads.query)
    # print(view_log)
    
    context = {
        'recent_ads' : recent_ads,
        'featured_ads' : featured_ads,
    }

    return render(request, 'pages/index.html', context)

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')



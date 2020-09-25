from ads.models import Ads, Category

def footer_recent_ads(request):
    ads = Ads.objects.filter(is_active=True).order_by('-date_created')[0:2]
    return {
        'footer_recent_ads' : ads
    }

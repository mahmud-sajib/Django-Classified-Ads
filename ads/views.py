from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Count
# Model Forms.
from .forms import PostAdsForm
# Create your views here.


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

# Post ads view
def post_ads(request):
    # User Post form.
    form = PostAdsForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            # title = request.POST.get('title')
            # description = request.POST.get('description')
            # price = request.POST.get('price')
            # state = request.POST.get('state')
            # city = request.POST.get('city')
            # category = request.POST.get('category')
            # condition = request.POST.get('condition')
            # brand = request.POST.get('brand')
            # image = request.POST.get('image')
            # phone = request.POST.get('phone')

            # ads = Ads.objects.create(author=request.user.author, title=title, description=description, price=price, state=state, city=city, category=category, condition=condition, brand=brand, image=image, phone=phone)
            
            # ads.save()
            
            return redirect('home')
    else:
        form = PostAdsForm(request.POST or None, request.FILES or None)

    context = {'form': form}
   
    return render(request, 'ads/post-ads.html', context)

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








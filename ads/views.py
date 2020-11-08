from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Count
# Model Forms.
from .forms import PostAdsForm
from django.contrib.auth.forms import User
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail

# importing messages
from django.contrib import messages

from ads.models import Author
# Create your views here.

# Post ads view
@login_required(login_url='login')
def post_ads(request):
    if request.method == 'POST':
        # Get ad title
        title = request.POST.get('title')

        # Get ad description
        description = request.POST.get('description')

        # Get ad category
        category = request.POST.get('category')
        # Check if the category exists
        category_check = Category.objects.filter(category_name=category).exists()
        if category_check:
            c = Category.objects.get(category_name=category) # Get the category if exists
        else:
            c = Category.objects.create(category_name=category) # Create the category
        
        # Get ad price
        price = request.POST.get('price')
        
        # Get ad condition
        condition = request.POST.get('condition')
        
        # Get user's living state
        state = request.POST.get('state')
        # Check if the state exists
        state_check = State.objects.filter(state_name=state).exists()
        if state_check:
            s = State.objects.get(state_name=state) # Get the state if exists
        else:
            s = State.objects.create(state_name=state) # Create the state

        # Get user's living city
        city = request.POST.get('city')
        # Check if the city exists
        city_check = City.objects.filter(city_name=city).exists()
        if city_check:
            ci = City.objects.get(city_name=city) # Get the city if exists
        else:
            ci = City.objects.create(city_name=city) # Create the city

        # Get ad brand
        brand = request.POST.get('brand')

        # Get user's phone
        phone = request.POST.get('phone')

        # Get ad video
        video = request.POST.get('video')

        # Get image files length
        length = request.POST.get('length')

        # Create the ad
        ads = Ads.objects.create(author=request.user.author, title=title, description=description, price=price, category=c, condition=condition, state=s, city=ci, brand=brand, phone=phone, video=video)

        # Attach the images with the associated ad
        for file_num in range(0, int(length)):
            AdsImages.objects.create(
                ads=ads,
                image=request.FILES.get(f'images{file_num}')
            )
        
        # Send email notificaton to Admin
        mail_subject = "New Ads submitted"
        sender_email = request.user.email
        message = f"Dear Admin, you received a new ads request from {sender_email}"
        print(message)
        to_email = settings.EMAIL_HOST_USER
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        
        send_mail(
            mail_subject,
            message,
            from_email,
            to_list,
            fail_silently=False,
        )
        
    return render(request, 'ads/post-ads.html')

# Ads listing view
def ads_listing(request):
    ads_listing = Ads.objects.all()
    category_listing = Category.objects.annotate(total_ads=Count('ads')).order_by('category_name')

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

# Ads state archive view
def ads_state_archive(request, slug):
    state = get_object_or_404(State, slug=slug)
    ads_by_state = Ads.objects.filter(state=state)

    context = {
        'state' : state,
        'ads_by_state' : ads_by_state
    }

    return render(request, 'ads/state-archive.html', context)

# Ads city archive view
def ads_city_archive(request, slug):
    city = get_object_or_404(City, slug=slug)
    ads_by_city = Ads.objects.filter(city=city)

    context = {
        'city' : city,
        'ads_by_city' : ads_by_city
    }

    return render(request, 'ads/city-archive.html', context)

# Ads author archive view
def ads_author_archive(request, pk):
    author = get_object_or_404(Author, pk=pk)
    ads_by_author = Ads.objects.filter(author=author)

    context = {
        'author' : author,
        'ads_by_author' : ads_by_author
    }

    return render(request, 'ads/author-archive.html', context)

# Ads search/filter view
def ads_search(request):

    state = request.GET.get('state_name')
    category = request.GET.get('category_name')

    if state:
        ads_search_result = Ads.objects.filter(state__state_name=state)
    elif category:
        ads_search_result = Ads.objects.filter(category__category_name=category)
    else:
        ads_search_result = Ads.objects.filter(state__state_name=state).filter(category__category_name=category)
    
    context = {
        'ads_search_result':ads_search_result
    }

    return render(request, 'ads/ads-search.html', context)

# Ads delete view
@login_required(login_url='login')
def ads_delete(request, pk):
    ad = get_object_or_404(Ads, pk=pk)
    ad.delete()
    return redirect("dashboard")










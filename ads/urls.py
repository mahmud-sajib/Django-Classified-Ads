from django.urls import path

from .import views

urlpatterns = [
    path('post-ads/', views.post_ads, name='post-ads'),
    path('ads-listing/', views.ads_listing, name='ads-listing'),
    path('ads-detail/', views.ads_detail, name='ads-detail'),
]
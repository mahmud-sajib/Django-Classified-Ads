from django.urls import path

from .import views

urlpatterns = [
    path('post-ads/', views.post_ads, name='post-ads'),
    path('ads-listing/', views.ads_listing, name='ads-listing'),
    path('ads/<int:pk>/', views.ads_detail, name='ads-detail'),
    path('ads/<int:pk>/delete/', views.ads_delete, name='ads-delete'),
    path('category/<slug:slug>/', views.ads_category_archive, name='category-archive'),
    path('state/<slug:slug>/', views.ads_state_archive, name='state-archive'),
    path('city/<slug:slug>/', views.ads_city_archive, name='city-archive'),
    path('author/<int:pk>/', views.ads_author_archive, name='author-archive'),
    path('ads-search/', views.ads_search, name='ads-search'),
]
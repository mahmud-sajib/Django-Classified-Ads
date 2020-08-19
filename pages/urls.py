from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('terms-of-service/', views.terms_of_service, name='terms-of-service'),
    path('contact/', views.contact, name='contact'),
]
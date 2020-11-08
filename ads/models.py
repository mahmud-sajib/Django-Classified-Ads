from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
# Default User model
from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField

# Create your models here.

# Author Model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default="default-profile-pic.png", upload_to='uploads/profile-pictures', null=True)

    def __str__(self):
        return self.user.username

# Ads Model
class Ads(models.Model):
    
    CONDITION = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True) 
    condition = models.CharField(max_length=100, choices=CONDITION)
    brand = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    video = EmbedVideoField(null=True, blank=True) 
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Classified Ads"

    def __str__(self):
        return self.title

# State Model
class State(models.Model):
    state_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    # overriding save method to add slug field from state name if not provided
    def save(self, *args, **kwargs):
        if not self.slug and self.state_name:
            self.slug = slugify(self.state_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "States"

    def __str__(self):
        return self.state_name

# City Model
class City(models.Model):
    city_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    # overriding save method to add slug field from city name if not provided
    def save(self, *args, **kwargs):
        if not self.slug and self.city_name:
            self.slug = slugify(self.city_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='uploads/category', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    # overriding save method to add slug field from category name if not provided
    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

# Image Model
class AdsImages(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', default=None)

    def __str__(self):
        return self.ads.title

    class Meta:
        verbose_name_plural = 'Classified Ads Images'

# Top Banner Model
class AdsTopBanner(models.Model):
    title = models.CharField(max_length=200, default="Place Your Ad", blank=True)
    image = models.ImageField(upload_to='banners/%Y/%m/%d', default=None)

    def __str__(self):
        return self.title

# Right Banner Model
class AdsRightBanner(models.Model):
    title = models.CharField(max_length=200, default="Place Your Ad", blank=True)
    image = models.ImageField(upload_to='banners/%Y/%m/%d', default=None)

    def __str__(self):
        return self.title

# Bottom Banner Model
class AdsBottomBanner(models.Model):
    title = models.CharField(max_length=200, default="Place Your Ad", blank=True)
    image = models.ImageField(upload_to='banners/%Y/%m/%d', default=None)

    def __str__(self):
        return self.title

    



    
    


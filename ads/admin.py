from django.contrib import admin
from .models import Author, Ads, State, City, Category, AdsImages, AdsTopBanner, AdsRightBanner, AdsBottomBanner
from django.utils.html import format_html

# Register your models here.

class AdsImagesAdmin(admin.StackedInline):
    model = AdsImages

class AdsAdmin(admin.ModelAdmin):
    
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="40">'.format(object.image.url))
    
    # Display columns in horizontal list
    list_display = ('id', 'title', 'price', 'author', 'category', 'date_created', 'is_featured', 'is_active')
    
    # Columns having links
    list_display_links = ('id', 'title')

    # Editable columns
    list_editable = ('is_featured', 'is_active')

    # Searchable columns
    # search_fields = ('title', 'price', 'state', 'category')

    # Filterable columns
    # list_filter = ('price', 'date_created', 'state', 'is_featured')

    inlines = [AdsImagesAdmin]

class AdsImagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ads, AdsAdmin)
admin.site.register(AdsImages, AdsImagesAdmin)

admin.site.register(Author)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(AdsTopBanner)
admin.site.register(AdsRightBanner)
admin.site.register(AdsBottomBanner)

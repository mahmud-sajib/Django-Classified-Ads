from django.contrib import admin
from .models import Ads, Category, AdsImages
from django.utils.html import format_html

# Register your models here.

class AdsAdmin(admin.ModelAdmin):
    
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40">'.format(object.image.url))
    
    # Display columns in horizontal list
    list_display = ('id', 'thumbnail', 'title', 'price', 'date_created', 'state', 'is_featured')
    
    # Columns having links
    list_display_links = ('id', 'thumbnail', 'title')

    # Editable columns
    list_editable = ('is_featured',)

    # Searchable columns
    # search_fields = ('title', 'price', 'state', 'category')

    # Filterable columns
    list_filter = ('price', 'date_created', 'state', 'is_featured')

    

admin.site.register(Ads, AdsAdmin)
# admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(AdsImages)
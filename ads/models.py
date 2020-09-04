from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Ads(models.Model):

    STATE = (
        ('Al', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    CONDITION = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    )


    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, choices=STATE)
    city = models.CharField(max_length=100)

    """ models.SET_NULL : Deleting an category will set the category field of ads as NULL """
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True) 
    condition = models.CharField(max_length=100, choices=CONDITION)
    brand = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True) 
    phone = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Classified Ads"

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='uploads/category', blank=True)
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


class AdsImages(models.Model):

    """ models.CASCADE: Deleting an ads will delete the associated images """
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='uploads/%Y/%m/%d' , blank=True , null=True)

    def __str__(self):
        return self.ads.title

    class Meta:
        verbose_name_plural = 'Classified Images'
    



    
    


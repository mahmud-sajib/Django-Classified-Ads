from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Ads(models.Model):

    STATE = (
        ('AL', 'Alabama'),
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

    CATEGORY = (
        ('Outfitter Operations (Find a hunt)', 'Outfitter Operations (Find a hunt)'),
        ('Hunting property for sale', 'Hunting property for sale'),
        ('Hunting land for lease & leases wanted ', 'Hunting land for lease & leases wanted'),
        ('Hunting dogs for sale & training', 'Hunting dogs for sale & training'),
        ('Guide jobs, Ranch manager jobs & camp staff', 'Guide jobs, Ranch manager jobs & camp staff'),
        ('Hunting vehicles & ATVs for sale', 'Hunting vehicles & ATVs for sale'),
        ('Breeder bucks & Breeding services', 'Breeder bucks & Breeding services'),
        ('Exotics for sale & Exotics wanted', 'Exotics for sale & Exotics wanted'),
        ('Archery', 'Archery'),
        ('Camouflage & Outerwear', 'Camouflage & Outerwear'),
        ('Blinds & Stands', 'Blinds & Stands'),
        ('Feeders', 'Feeders'),
        ('Waterfowl', 'Waterfowl'),
        ('Aviation services', 'Aviation services'),
        ('Footwear', 'Footwear'),
        ('Property improvements & services', 'Property improvements & services'), 
        ('Fire arm accessories', 'Fire arm accessories'),
        ('Game calls', 'Game calls'),
        ('Traps and Trapping services', 'Traps and Trapping services'),
        ('Wildlife Biology and Surveying', 'Wildlife Biology and Surveying'),
        ('Gun safes', 'Gun safes'),
        ('Merchandise', 'Gun safes'),
        ('Business for sale', 'Business for sale'),
        ('Miscellaneous', 'Miscellaneous'),
    )

    CONDITION = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    )


    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, choices=STATE)
    city = models.CharField(max_length=100)
    specification = RichTextField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    condition = models.CharField(max_length=100, choices=CONDITION)
    brand = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True) 
    phone = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Classified Ads"

    def __str__(self):
        return self.title

    
    


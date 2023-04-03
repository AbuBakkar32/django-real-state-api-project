from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils.timezone import now

from realtor.models import Agent
from PIL import Image


# Create your models here.
class Home(models.Model):
    class SaleType(models.TextChoices):
        FOR_RENT = 'RENT', 'Rent'
        FOR_SALE = 'SALE', 'Sale'

    class HomeType(models.TextChoices):
        HOUSE = 'HOUSE', 'House'
        APARTMENT = 'APARTMENT', 'Apartment'
        Flat = 'FLAT', 'Flat'
        TOWNHOUSE = 'TOWNHOUSE', 'Townhouse'

    agent = models.ForeignKey(Agent, on_delete=DO_NOTHING, related_name='agents')
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=100, choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=100, choices=HomeType.choices, default=HomeType.HOUSE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='home/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.slug


class ImageFiles(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='home/%Y/%m/%d/', blank=True)

    def save(self, *args, **kwargs):
        super(ImageFiles, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

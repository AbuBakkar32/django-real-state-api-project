from django.db import models
from datetime import datetime


# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=200)
    biodata = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    image = models.ImageField(upload_to='realtor')
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

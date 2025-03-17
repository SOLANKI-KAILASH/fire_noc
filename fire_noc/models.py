from django.db import models
import datetime
from cloudinary.models import CloudinaryField

class FireNOCSubmission(models.Model):
    name = models.CharField(max_length=30,default="Unknown")
    email=models.EmailField(default="default@gmail.com")
    phone=models.CharField(max_length=13,default="Unknown")
    date=models.DateField(default=datetime.date.today)
    org_name=models.CharField(max_length=255,default="Unknown")
    org_address = models.CharField(max_length=255)
    fire_extinguisher = CloudinaryField("fire_extinguisher")
    fire_exit = CloudinaryField("fire_exit")
    fire_safety_sign = CloudinaryField("fire_safety_sign")
    water_infrastructure = CloudinaryField("water_infrastructure")
    noc_pdf_url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.org_address

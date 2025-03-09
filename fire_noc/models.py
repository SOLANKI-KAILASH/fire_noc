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
    fire_extinguisher = CloudinaryField("fire_noc")
    fire_exit = CloudinaryField("fire_noc")
    fire_safety_sign = CloudinaryField("fire_noc")
    water_infrastructure = CloudinaryField("fire_noc")

    def __str__(self):
        return self.org_address

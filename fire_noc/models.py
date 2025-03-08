from django.db import models
from cloudinary.models import CloudinaryField

class FireNOCSubmission(models.Model):
    site_address = models.CharField(max_length=255)
    fire_extinguisher = CloudinaryField("fire_noc")
    fire_exit = CloudinaryField("fire_noc")
    fire_safety_sign = CloudinaryField("fire_noc")
    water_infrastructure = CloudinaryField("fire_noc")

    def __str__(self):
        return self.site_address

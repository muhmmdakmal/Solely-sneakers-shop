from django.db import models
import uuid
import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    time = models.DateField(default=datetime.date.today)# Menampilkan waktu
    image = models.ImageField(upload_to='media/product_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def image_url(self):
        if self.image:
            return self.image.url
        return None
    

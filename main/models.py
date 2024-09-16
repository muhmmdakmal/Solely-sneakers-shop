from django.db import models
import uuid
import datetime

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    time = models.DateField(default=datetime.date.today)# Menampilkan waktu
    rating_barang = models.IntegerField() # Rating untuk barang


    def __str__(self):
        return self.name

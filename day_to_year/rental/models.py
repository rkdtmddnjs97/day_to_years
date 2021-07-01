from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()

# Create your models here.
class Rental(models.Model): 
    product = models.CharField(max_length=20)
    writer = models.ForeignKey(User,on_delete=CASCADE,related_name="rentals")
    price = models.IntegerField()
    location_city = models.CharField(max_length=10)
    location_detail = models.CharField(max_length=10)
    rentterm = models.IntegerField()
    information = models.CharField(max_length=300)
    images = models.ImageField(default ="../static/rental/img/daytoyear.jpg", blank=True, upload_to="images/", null=True)
    chatting = models.CharField(max_length=300,default= '')

    def __str__(self):
        return self.product

            

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE, related_name= "like")
    rental = models.ForeignKey(Rental,on_delete=CASCADE, related_name= "like")
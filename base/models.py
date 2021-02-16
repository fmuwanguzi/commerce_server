from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    #SET_NULL means if the user gets deleted the product won't get deleted
    #blank determines whether the field will be required in forms
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    #image =
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description =  models.TextField(null=True, blank=True)
    rating =  models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    #this overidies the original field Django would set up. 
    # We do this to match with what we currently have on the front end
    #editable is false so no one can edit it
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    
#review model has relationship with the user and product
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.rating)  #have to make the rating a string or the admin tab will give us an error

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod =  models.CharField(max_length=200, null=True, blank=True)
    taxPrice =
    shippingPrice =
    totalPrice =
    isPaid =
    paidAt =
    isDelivered =
    deliveredAt =
    createdAt =
    _id = models.AutoField(primary_key=True, editable=False)
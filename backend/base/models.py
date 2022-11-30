from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(null=True)
    brand = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    numReviews = models.IntegerField(null=False, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    countInStock = models.IntegerField(null=False, default=0)
    createdAt = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    comment = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return str(self.rating)


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=50, null=False, blank=False)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    isPaid = models.BooleanField(null=False, default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True)
    isDelivered = models.BooleanField(null=False, default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return str(self.createdAt)


class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    qty = models.IntegerField(null=False, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    image = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class ShippingAddress(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    postalCode = models.CharField(max_length=7, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)

    def __str__(self) -> str:
        return self.address

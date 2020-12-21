from datetime import datetime

from django.db import models

# Create your models here.


class LoginInfo(models.Model):
    fname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class HairStyles(models.Model):
    style_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    style_img = models.ImageField(default='',blank=True)


class Booking(models.Model):
    booker_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booked_date = models.DateField(default=datetime.now())
    mobile = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0)
    product_img = models.ImageField()
    product_gender = models.CharField(max_length=10)
    product_stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name, self.product_stock


class Cart(models.Model):
    user_id = models.ForeignKey(LoginInfo, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_in_cart = models.BooleanField(default=True)


class Billing(models.Model):
    user_id = models.ForeignKey(LoginInfo, on_delete=models.CASCADE)
    totalpay = models.IntegerField(default=0)
    billingdate = models.DateField(default=datetime.now())
    is_active = models.BooleanField(default=True)


class BillingItem(models.Model):
    billingid = models.ForeignKey(Billing, on_delete=models.CASCADE)
    itemid = models.ForeignKey(Product, on_delete=models.CASCADE)


class BillingAddress(models.Model):
    billingid = models.ForeignKey(Billing, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)


class BillingCard(models.Model):
    billingid = models.ForeignKey(Billing, on_delete=models.CASCADE)
    cardname = models.CharField(max_length=200)
    cardnumber = models.IntegerField(default=0)
    cardcvv = models.IntegerField(default=0)
    cardexp = models.CharField(max_length=100)
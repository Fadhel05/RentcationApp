
from django.db import models



class CustomerModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20,blank=False,null=False)
    email = models.EmailField(max_length=20,unique=True)
    password = models.CharField(max_length=20,blank=False,null=False)
    password_confirmation = models.CharField(max_length=20,blank=False,null=False)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    house_number = models.IntegerField(blank=True,null=True)
    phone_number = models.IntegerField(blank=False,null=False)
    class Meta:
        db_table = 'user'



class PaymentModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class UserModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE,related_name="id_user")

class CategoryModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class ProductModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_user = models.ManyToManyField(UserModel,related_name="id_product",null=True,blank=True)
    id_category = models.ForeignKey(CategoryModel,null=True,on_delete=models.SET_NULL,blank=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    price = models.IntegerField(default=0,max_length=15)
    description = models.TextField(blank=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)

class DestinationModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    id_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ImageModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_product = models.ForeignKey(ProductModel,on_delete=models.SET_NULL,blank=True,null=True)
    id_destination = models.ForeignKey(DestinationModel,on_delete=models.CASCADE,null=True,blank=True)
    imagebase64 = models.CharField(max_length=2048)
    imagename = models.CharField(max_length=50,null=True,blank=True)


class BookingModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    id_customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE,null=True,blank=True)
    id_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    data_id = models.IntegerField()
    data_name = models.CharField(max_length=255)
    product_count = models.IntegerField()
    booking_in = models.DateField(auto_now_add=False,auto_now = False,auto_created=False)
    booking_out = models.DateField(auto_created=False,auto_now_add=False,auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)

class CheckoutModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_booking = models.ForeignKey(BookingModel,on_delete=models.CASCADE,null=False,blank=False)
    id_payment = models.ForeignKey(PaymentModel,on_delete=models.CASCADE,null=True,blank=True)
    total_payment = models.IntegerField(null=True,blank=True)
    checkout_date = models.DateTimeField(auto_now_add=True)


class ReviewModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_booking = models.ForeignKey(BookingModel,on_delete=models.CASCADE)
    id_customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    rating = models.IntegerField(null=False,blank=False)
    comment = models.CharField(max_length=255,null=True,blank=True)
    review_date = models.DateTimeField(auto_now_add=True)



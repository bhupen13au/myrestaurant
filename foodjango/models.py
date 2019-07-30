from django.db import models

# Create your models here.
class Dish(models.Model):
    d_name = models.CharField(max_length=30)
    d_catagory = models.BooleanField(default=False,name='Non_Veg')
    d_price = models.IntegerField()
    d_qty = models.IntegerField()

    class Meta:
        db_table="Dishes"


class User_details(models.Model):
    u_name = models.CharField(max_length=30)
    u_dob = models.CharField(max_length=30)
    u_address = models.CharField(max_length=30)
    u_email = models.CharField(max_length=30)
    u_phone = models.IntegerField()

    class Meta:
        db_table="User_Details"

from django.db import models
from unixtimestampfield.fields import UnixTimeStampField
from datetime import date
# Products Model
class Product  (models.Model):
    
    # Name of the product
    name = models.CharField(max_length=200, verbose_name='Product Name')
    
    # price of product
    price = models.FloatField(verbose_name='price in USD')

class Transaction(models.Model):

    #Transaction id -> default id from django

    # reference to product
    product = models.ForeignKey(Product,  on_delete=models.DO_NOTHING)

    #amount sold -> quantity
    amount = models.PositiveIntegerField(help_text='Please enter amount')

    #created date
    #created = UnixTimeStampField(auto_now_add=True)
    created = models.DateField(default=date.today)

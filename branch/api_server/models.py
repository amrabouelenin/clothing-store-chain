from django.db import models
from unixtimestampfield.fields import UnixTimeStampField
import time
from datetime import date
# Create services call model
class ServicesCall(models.Model):

    # id of the call - use default id from django
    
    # status
    status = models.BooleanField(default=False) 

    # expected date  -> unixtimestamp format
    expected_date = models.DateField(default=date.today)
    
    # actual date -> unixtimestamp format
    actual_date = models.DateField(null=True, blank=True, auto_now_add=False)

    # comment
    comments = models.CharField(max_length=200)

    # revenue
    revenue = models.IntegerField()

    # loss
    loss = models.IntegerField()



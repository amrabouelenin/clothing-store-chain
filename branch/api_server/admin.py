from django.contrib import admin
from products.models import Product , Transaction
from .models import ServicesCall
# Register your models here.
admin.site.register(Transaction)
admin.site.register(ServicesCall)

admin.site.register(Product)
# Register your models here.

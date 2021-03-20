from django.contrib import admin
from .models import DailyRevenue, Branch
# Register your models here.
admin.site.register(Branch)
admin.site.register(DailyRevenue)

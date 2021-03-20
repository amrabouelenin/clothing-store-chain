from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=264, unique= True, help_text = "Please write the name of branch") 

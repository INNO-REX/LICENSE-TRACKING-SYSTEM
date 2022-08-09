from datetime import date
from pickle import FALSE, TRUE
import django
from django import forms
from django.db import models
from django.contrib import admin 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class License(models.Model):
    #item_description = models.CharField(max_length=30)
    item_description  = models.CharField(max_length=50,unique=True)
    Installation_Date =models.DateTimeField()
    Expiry_Date = models.DateTimeField()
   
# Responsible_person= models.CharField(max_length=30)
    PERSON_SELECT = (
        ('System Admin', 'System Admin'),
        ('Network Admin', 'Network Admin'),
        ('o', 'Other'),
    )
    Responsible_person=models.CharField(max_length=50,choices=PERSON_SELECT)
   
   
    #active = models.BooleanField()
    #def __str__(self):
        #return self.item_description




#def __str__(self):
   # return f"{self.Name} @ ${self.Amount} every {self.PayDate} of the month"

   
  
  
    

created = models.DateTimeField(auto_now_add=True)
updated = models.DateTimeField(auto_now_add=True)

#fields = (TRUE, 'gender',)

#radio_fields = {'gender': admin.VERTICAL}
    


# class License(models.Model):
#     item_name = models.CharField(max_length=30)
#     expiry_date = models.IntegerField() 
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)
    
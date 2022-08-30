from argparse import OPTIONAL
from datetime import date
from pickle import FALSE, TRUE
import django
from django import forms
from django.db import models
from django.contrib import admin 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class License(models.Model):
    item_description  = models.CharField(max_length=50,unique=True)
    Installation_Date =models.DateField()
    Expiry_Date = models.DateField()
    # license.created = models.DateField(auto_now_add=True)
    # license.updated = models.DateField(auto_now_add=True)
    
    # Responsible_person= models.CharField(max_length=30)
    PERSON_SELECT = (
        ('System Admin', 'System Admin'),
        ('Network Admin', 'Network Admin'),
        ('o', 'Other'),
    )
    Responsible_person=models.CharField(max_length=50,choices=PERSON_SELECT)

    def age_in_days(self):
        today = date.today()
        result = self.Expiry_Date- today
        return result.days
 
# 
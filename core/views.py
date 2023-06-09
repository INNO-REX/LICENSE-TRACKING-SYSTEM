#import datetime
from email import message
from email.message import EmailMessage
from msilib.schema import SelfReg
import smtplib
from typing import Any
# from typing_extensions import Self
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.mail import EmailMessage
from django.utils.timezone import localdate
from datetime import datetime





from core.forms import LicenseForm
from .models import License

class LicenseListView(ListView):
    model = License
    all_licenses= License.objects.all()
    print(all_licenses)
    for license in all_licenses:
        today=datetime.now().date()
        Expiry_Date=license.Expiry_Date
        if(Expiry_Date-today).days<=10:
            print("The license:"+str(license.id)+"is about to Expire in" +str((Expiry_Date-today)  .days)+"days") 
      
        def get_context_data(self, **kwargs):
            context= super().get_context_data(**kwargs)

        #licenses that meet the condition##################################
            meetcondition=[]
            meet_condition_licenses=""
            all_licenses= License.objects.all()
            for license in all_licenses:
                today=datetime.now().date()
                Expiry_Date=license.Expiry_Date
                if(Expiry_Date-today).days<=10:
                    meetcondition.append(license.Expiry_Date)
                    meet_condition_licenses = License.objects.filter(Expiry_Date__in=meetcondition)
                    print(license.Expiry_Date)
            context['meet_condition_licenses'] = meet_condition_licenses
            context['all_licenses'] = all_licenses
            return context
            



        #mail=======================================================auto send---
        # 
        # 
        # 
        print("here in Notifications")
        mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        #print(mailServer.ehlo())
        mailServer.starttls()
        #print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        print("conecting...")
        #
        email_to=[]
        # email_to.append("wwrandazzo@gmail.com")
        email_to.append("innocent94.kasoma@gmail.com")
        # create  e-mail
        subject='License mail notification'
        message=""
        
       
           
              
      
                #  
            # message=""
        Expiry_Date=license.Expiry_Date
        if(Expiry_Date-today).days<=10:
                    #==============================================
                    
          

                    #needed------------------------------
                    message+= 'You have received this Notification because the License for'' {}'.format( license.item_description ) +  ( '  will Expire on | ') + str((Expiry_Date))
                    #message+="The license:"+str(license.id)+"is about to Expire in" +str((Expiry_Date-today).days)+"days"
                    subject = 'NOTIFICATION OF ELIAM LICENSE'
           
       
        
      
                    email = EmailMessage(subject, message,settings.EMAIL_HOST_USER,email_to)
        # send e-mail
                    email.send()
        print("email sent OK")

        




def get_queryset(self):
    dia_de_hoy= datetime.now(). date()
    context = License.objects.filter(Expiry_Date_gte=dia_de_hoy).order_by('-id')
    return context

def license_form(request):
    return render(request, 'core/base.html')

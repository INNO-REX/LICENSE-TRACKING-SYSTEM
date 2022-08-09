import datetime
from email.message import EmailMessage
import smtplib
from typing import Any
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.mail import EmailMessage


from core.forms import LicenseForm
from .models import License

class LicenseListView(ListView):
    model = License

#create your views here.
class LicenseCreateview(CreateView):
   model = Licenseform_class =LicenseForm
   success_url =reverse_lazy('create')

def get_queryset(self):
    dia_de_hoy= datetime.now(). date()
    context = License.objects.filter(Expiry_Date_gte=dia_de_hoy).order_by('-id')
    return context

def license_form(request):
    return render(request, 'core/base.html')

#def  license_form(request):
    #return render(request, 'core/licence_form.html')

#Notification email view
class notificacionMailView(View):
    def get(self,request,*args,**kwargs):
        print("here in Notifications")
        mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        #print(mailServer.ehlo())
        mailServer.starttls()
        #print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        print("conectando...")
        #
        email_to=[]
        email_to.append("wwrandazzo@gmail.com")
        # create  e-mail
        subject='license id{}'.format(self.kwargs['id'])
        # subject = 'NOTIFICATION OF LICENSE via email'
        message = 'This is a notificaicon because the license is about to expire.'
        email = EmailMessage(subject, message,settings.EMAIL_HOST_USER,email_to)
        # send e-mail
        email.send()
        print("email sent OK")
       
        return redirect('list') 
    
    
    
    
    
    
    
    all_licenses= License.objects.all()
        for license in all_licenses:
         tiempo_transcurrido=license.Expiry_Date-datetime.datetime.now
         print(datetime.timedelta(minutes=10))
         print(license.Expiry_Date)
         print(tiempo_transcurrido)
        if(license.Expiry_Date <=tiempo_transcurrido):
          print("The license:"+ str(license.id) + " is about to expire in 10 minutes" )
    
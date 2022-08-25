#import datetime
from email import message
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
        if(Expiry_Date-today).days<=2:
            print("The license:"+str(license.id)+"is about to Expire in" +str((Expiry_Date-today).days)+"days") 
        print(today)
        print(Expiry_Date)
        print(Expiry_Date-today)
        

       
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
        # email_to.append("wwrandazzo@gmail.com")
        email_to.append("innocent94.kasoma@gmail.com")
        # create  e-mail
        subject='license id {}'.format(self.kwargs['id'])
        message=""
        all_licenses= License.objects.all()
        print(all_licenses)
        for license in all_licenses:
            today=datetime.now().date()
            Expiry_Date=license.Expiry_Date
            if(Expiry_Date-today).days<=4:
               
                message+="The license:" + str(license.id)+ "is about to Expire in" + str ((Expiry_Date-today).days) + "days"
               # print("The license:"+str(license.id)+"is about to Expir in" +str((Expiry_Date-today).days)+"days") 
        #subject = 'NOTIFICATION OF ELIAM LICENSE'
        message = 'This is a notificaicon because the license is about to expire.'
        email = EmailMessage(subject, message,settings.EMAIL_HOST_USER,email_to)
        # send e-mail
        email.send()
        print("email sent OK")
     
        return redirect('list') 
  
    def get_context_data(self, **kwargs):
            context= super().get_context_data(**kwargs)
        #licenses that meet the condition
            meetcondition=[]
            all_licenses= License.objects.all()
            for license in all_licenses:
                today=datetime.now().date()
            Expiry_Date=license.Expiry_Date
            if(Expiry_Date-today).days<=4:
                meetcondition.append(license.pk)
            meet_condition_licenses = License.objects.filter(pk__in=meetcondition)
            return context
    
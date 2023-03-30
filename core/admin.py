
from django.contrib import admin
from core.models import License
from django.contrib.auth.models import Group


 
# Register your models here.
admin.site.register(License)
admin.site.unregister(Group)
admin.site.site_header = 'LICENSE TRACKING SYSTEM'

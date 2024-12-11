from django.contrib import admin
from app.models import *

# Register your models here.

class database(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddress"]


admin.site.register(employees,database)

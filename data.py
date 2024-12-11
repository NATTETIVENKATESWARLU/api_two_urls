import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","api_methods.settings")
import django

django.setup()


#--------------------------------------------------------------------------------
from app.models import *
from faker import Faker
import random
data=Faker()

for i in range(10):
    en=random.randint(1,200)
    enam=data.name()
    sal=random.choice([10000,12000,130000,140000])
    eadd=data.address()
    ra=employees.objects.get_or_create(eno=en,ename=enam,esal=sal,eaddress=eadd)[0]
    ra.save()
    print(en,enam,sal,eadd)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','databaseproj.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
fake = Faker()
def display(n):
    for i in range(n):
        feno= randint(1000,9999)
        fename = fake.name()
        fesal = randint(10000,99999)
        feaddr = fake.city()
        empl_rec = Employee.objects.get_or_create(eno=feno,ename = fename, esal = fesal, eaddr =feaddr)
display(20)


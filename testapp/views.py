from django.shortcuts import render
from testapp.models import Employee

def Empdata(request):
    emp_data = Employee.objects.all()
    my_dict = {'emp_data':emp_data}
    return render(request,'testapp/show.html',context = my_dict)
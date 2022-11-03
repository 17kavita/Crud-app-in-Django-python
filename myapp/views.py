from django.shortcuts import redirect,render
from django.views import View
from .models import Employee
from .forms import AddEmployeeForm

class Home(View):
    def get(self,request):
        emp_data=Employee.objects.all()
        return render(request,'core/home.html',{'empdata':emp_data})

class Add_Employee(View):
    def get(self,request):
        fm=AddEmployeeForm()
        return render(request,'core/add_employee.html',{'form':fm})

    def post(self,request):
        fm=AddEmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add_employee.html',{'form':fm})

class Delete_Employee(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        empdata=Employee.objects.get(id=id)
        empdata.delete()
        return redirect('/')

from django.urls import path
from .views import Home,Add_Employee,Delete_Employee
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('/add_employee/',Add_Employee.as_view(),name='add_employee'),
    path('/delete_employee/',Delete_Employee.as_view(),name='delete_employee')
]
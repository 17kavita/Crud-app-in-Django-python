from django import forms
from .models import Employee


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=("f_name","l_name","phone","email")
        widgets ={
            'f_name':forms.TextInput(attrs={'class':'form-control'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
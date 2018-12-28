from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        input_sal=self.cleaned_data['esal']
        if input_sal<1000:
            raise forms.ValidationError(" the minimum salary should br 2000 .")
        return input_sal
    class Meta:
        model=Employee
        fields='__all__'

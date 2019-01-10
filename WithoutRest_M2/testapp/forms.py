from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    def clean_marks(self):
        input_marks=self.cleaned_data['marks']
        if input_marks < 40:
            raise forms.ValidationError('Min Marks are 40')
        else:
            return  input_marks
    class Meta:
        model=Student
        fields="__all__"

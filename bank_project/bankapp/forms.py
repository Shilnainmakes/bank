from django import forms
from django.forms import DateInput,EmailInput

from bankapp.models import Form, MaterialOption


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name','date_of_birth','age','gender','phone_number','email','address','district','branch','account_type']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'email': EmailInput(),
        }
    materials_provided=forms.ModelMultipleChoiceField(queryset=MaterialOption.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)




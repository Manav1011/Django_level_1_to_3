from django import forms
from django.core import validators


class basic_form(forms.Form):
    name=forms.CharField(max_length=256,required=True)
    age=forms.IntegerField(required=True)
    gender=forms.CharField(max_length=256,required=True)
    
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<=5:
            raise forms.ValidationError("Name must be greater than 5 characters")
        return name
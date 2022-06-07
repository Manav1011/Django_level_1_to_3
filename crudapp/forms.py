from django import forms
from django.core import validators
from .models import info
class basic_form(forms.Form):
    name=forms.CharField(max_length=256,required=True)
    age=forms.IntegerField(required=True)
    gender=forms.CharField(max_length=256,required=True)
    
    
class model_form(forms.ModelForm):
    class Meta:
        model=info
        fields='__all__'
        CHOICES = [('M','Male'),('F','Female')]
        widgets={'age':forms.NumberInput(),'gender':forms.RadioSelect(choices=CHOICES),'name':forms.TimeInput()}
        

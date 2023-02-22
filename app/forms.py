from django import forms
from app.models import *

class student(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    number=forms.IntegerField(min_value=10)

class data(forms.ModelForm):
    class Meta:
        model=college
        fields='__all__'
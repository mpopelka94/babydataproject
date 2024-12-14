from django import forms
from django.forms import ModelForm, TextInput
from .models import Baby

class DataEntryForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['name','age','allergy']
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Name',
            }),
            'age': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Age',
            }),
            'allergy': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Age',
            })
        }
from django import forms
from django.forms import ModelForm, TextInput
from .models import Baby, BabyEvent

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
                'placeholder':'Allergy',
            })
        }

class BabyEventForm(forms.ModelForm):
    class Meta:
        model = BabyEvent
        fields = ['name','diaper_change','meal','sleep','meds']
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'style':'width:500px;',
                'placeholder':'Name of Baby',
            }),
            'diaper_change': TextInput(attrs={
                'class':'form-control',
                'style':'width:500px;',
                'placeholder':'Diaper Change Details',
            }),
            'meal': TextInput(attrs={
                'class':'form-control',
                'style':'width:500px;',
                'placeholder':'Did Baby Eat?',
            }),
            'sleep': TextInput(attrs={
                'class':'form-control',
                'style':'width:500px;',
                'placeholder':'Did Baby Sleep?',
            }),
            'meds': TextInput(attrs={
                'class':'form-control',
                'style':'width:500px;',
                'placeholder':'Did you give Baby any meds?',
            })
        }
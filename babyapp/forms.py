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
        fields = ['name','diaper_change','meal','sleep']
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Name You are here',
            }),
            'diaper_change': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Diaper Change',
            }),
            'meal': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Meal',
            }),
            'sleep': TextInput(attrs={
                'class':'form-control',
                'style':'width:100px;',
                'placeholder':'Sleep',
            })
        }
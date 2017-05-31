from django import forms

from .models import usuario

class LibroModelForm(forms.ModelForm):
    class Meta:
        model=usuario
        fields=[
            "nombre",
            "progreso",
            "edad",
            "pcUser",
        ]
        labels={
            "nombre":"Cual es el nombre",
            "progreso":"Cual es tu progreso",
            "edad":"Cual es tu edad",
            "pcUser":"Como se llama el pc"
        }
        widgets={
            "nombre":forms.TextInput(attrs={'class':'form-control','placeholder':'Ponga el nombre'}),
            "progreso":forms.Textarea(attrs={'class':'form-control'}),
            "edad":forms.NumberInput(attrs={'class':'form-control'})
        }

# forms.py

from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del laboratorio'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'Ingrese la ciudad del laboratorio', 'class': 'clear-default'}),
            'pais': forms.TextInput(attrs={'placeholder': 'Ingrese el país del laboratorio', 'class': 'clear-default'})
        }
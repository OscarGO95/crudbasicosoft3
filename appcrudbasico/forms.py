from django.forms import ModelForm, Textarea, TextInput, URLInput
from appcrudbasico.models import Estudiante


class estudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['id','nombre','apellido','direccion', 'telefono','grado']
        widgets = {
            'id': TextInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido': TextInput(attrs={'class': 'form-control'}),
            'direccion': TextInput(attrs={'class': 'form-control'}),
            'telefono': TextInput(attrs={'class': 'form-control'}),
            'grado': TextInput(attrs={'class': 'form-control'})
        }
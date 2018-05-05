from django.forms import ModelForm, TextInput

from appcrudbasico.models import Maestros


class MaestrosForm(ModelForm):
    class Meta:
        model = Maestros
        fields = ['cedula', 'nombres', 'apellidos', 'direccion', 'materia']
        widgets = {
            'cedula': TextInput(attrs={'class': 'form-control'}),
            'nombres':TextInput(attrs={'class': 'form-control'}),
            'apellidos':TextInput(attrs={'class': 'form-control'}),
            'direccion':TextInput(attrs={'class': 'form-control'}),
            'materia':TextInput(attrs={'class': 'form-control'})
        }

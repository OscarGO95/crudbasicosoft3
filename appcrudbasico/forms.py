from appcrudbasico.models import Actividades
from django.forms import ModelForm, Textarea, TextInput, URLInput


class ActividadesForm(ModelForm):
    class Meta:
        model = Actividades
        fields = ['codigo', 'nombre', 'fecha_entrega', 'estado', 'nota']
        widgets = {
            'codigo': TextInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'fecha_entrega': TextInput(attrs={'class': 'form-control'}),
            'estado': TextInput(attrs={'class': 'form-control'}),
            'nota': TextInput(attrs={'class': 'form-control'}),
        }
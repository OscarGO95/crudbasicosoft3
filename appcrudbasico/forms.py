from django.forms import ModelForm, Textarea, TextInput, URLInput
from appcrudbasico.models import Materia


class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'profesor', 'intensidad']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'profesor': TextInput(attrs={'class': 'form-control'}),
            'intensidad': TextInput(attrs={'class': 'form-control'}),
        }
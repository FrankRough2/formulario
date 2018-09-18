from django.forms import ModelForm

## importamos nuestro modelo creado anteriormente

from .models import Formulario

class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'

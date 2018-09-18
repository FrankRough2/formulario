from django.db import models
from django.urls import reverse #generate urls from url patterns
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Formulario(models.Model):
    nombre = models.CharField(max_length=180)
    apellido_p = models.CharField(max_length=90)
    apellido_m = models.CharField(max_length=90)
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
### Y ASI SUCESIVAMENTE CON LOS OTROS CAMPOS DEL FORMULARIO
## OBVIAMENTE PUEDES AGREGAR DECORADORES Y VALIDADORES PARA CADA CAMPO





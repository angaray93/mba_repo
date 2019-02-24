from django import forms
from django.contrib import admin
#from django.forms import *
from django.forms import ModelForm, NumberInput, IntegerField
from django.forms.widgets import SelectDateWidget, DateInput
from django.forms.fields import DateField
from mba_sys.models import *

SEXO_OPTIONS = (
    ('F', 'Femenino'),
    ('M' , 'Masculino'),
)


class InstitucionForm(ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'

class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        labels = {
            'nrodocumento': 'Cedula de Identidad',
            'nro_contacto': 'Teléfono de Contacto',
            'nom_contacto': 'Nombre de Contacto',
            'fechaIngreso': 'Fecha de Ingreso',
        }

class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'
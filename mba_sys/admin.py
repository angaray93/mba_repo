from django.contrib import admin

from mba_sys.forms import *
from mba_sys.models import *

#--------------------------------------------------#

class InstitucionAdmin(admin.ModelAdmin):
    form = InstitucionForm
    list_display = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Institucion, InstitucionAdmin)

class CarreraAdmin(admin.ModelAdmin):
    form = CarreraForm
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

admin.site.register(Carrera, CarreraAdmin)

class AlumnoAdmin(admin.ModelAdmin):
    form = AlumnoForm
    list_display = ('apellidos',)
    search_fields = ('nrodocumento',)

admin.site.register(Alumno, AlumnoAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    form = PeriodoForm
    list_display = ('descripcion', 'year',)
    search_fields = ('descripcion', 'year')

admin.site.register(Periodo, PeriodoAdmin)
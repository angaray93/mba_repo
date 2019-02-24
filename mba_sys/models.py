from django.db import models
import datetime


class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, default='', unique=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return '%s ' % (self.nombre)

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=70, default='', unique=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        ordering = ["descripcion"]
        verbose_name_plural = "Carreras"

    def __str__(self):
        return '%s ' % (self.descripcion)


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30, default='')
    apellidos = models.CharField(max_length=30, default='')
    nrodocumento = models.CharField(max_length=15, default='', unique=True)
    edad = models.CharField(max_length=3, default='')
    sexo = models.CharField(max_length=70, default='')
    telefono = models.CharField(max_length=30, default='')
    nom_contacto = models.CharField(max_length=30, default='')
    nro_contacto = models.CharField(max_length=30, default='')
    fechaIngreso = models.DateTimeField(null=True, blank=True)
    comentarios = models.TextField(max_length=100, default='')

    class Meta:
        ordering = ["fechaIngreso"]
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(blank=True, null=True, default=1)
    descripcion = models.CharField(max_length=70, default='', unique=True)
    fechaInicio = models.DateTimeField(null=True, blank=True)
    fechaFin = models.DateTimeField(null=True, blank=True)
    year = models.IntegerField(default=datetime.datetime.today().year)

    class Meta:
        ordering = ["numero"]
        verbose_name_plural = "Periodos"

    def __str__(self):
        return '%s %s %s' % (self.numero, self.descripcion, self.year)




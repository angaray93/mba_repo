# Generated by Django 2.1.7 on 2019-02-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mba_sys', '0002_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(default='', max_length=70),
        ),
    ]

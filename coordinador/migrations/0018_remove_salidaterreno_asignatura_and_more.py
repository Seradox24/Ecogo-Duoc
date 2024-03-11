# Generated by Django 4.2 on 2024-03-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_nombreseccion_remove_asignatura_secciones_and_more'),
        ('coordinador', '0017_implemento_salidaterrenoimplemento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salidaterreno',
            name='asignatura',
        ),
        migrations.RemoveField(
            model_name='salidaterreno',
            name='seccion',
        ),
        migrations.AddField(
            model_name='salidaterreno',
            name='asignaturas',
            field=models.ManyToManyField(blank=True, related_name='salidas_terreno', to='core.asignatura'),
        ),
        migrations.AddField(
            model_name='salidaterreno',
            name='secciones',
            field=models.ManyToManyField(blank=True, to='core.seccion'),
        ),
    ]

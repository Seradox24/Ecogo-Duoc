# Generated by Django 4.2 on 2024-02-22 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0016_pronosticoclima_ultima_actualizacion_api'),
        ('alumno', '0005_remove_bajaestudiante_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bajada',
            name='salida_terreno',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='coordinador.salidaterreno'),
        ),
    ]

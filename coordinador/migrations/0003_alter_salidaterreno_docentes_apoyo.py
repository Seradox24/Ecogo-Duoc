# Generated by Django 4.2 on 2024-01-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('coordinador', '0002_actividad_alter_salidaterreno_anio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidaterreno',
            name='docentes_apoyo',
            field=models.ManyToManyField(blank=True, related_name='salidas_terreno_apoyo', to='core.usersmetadata'),
        ),
    ]

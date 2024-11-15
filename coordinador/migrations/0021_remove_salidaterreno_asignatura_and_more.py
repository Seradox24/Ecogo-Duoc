# Generated by Django 4.2 on 2024-03-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_seccion_usuarios'),
        ('coordinador', '0020_remove_salidaterreno_asignaturas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salidaterreno',
            name='asignatura',
        ),
        migrations.AddField(
            model_name='salidaterreno',
            name='asignaturas',
            field=models.ManyToManyField(blank=True, related_name='salidas_terreno', to='core.asignatura'),
        ),
        migrations.AlterField(
            model_name='salidaterreno',
            name='semestre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

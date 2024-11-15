# Generated by Django 4.2 on 2024-01-17 19:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('coordinador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='salidaterreno',
            name='anio',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(3000)]),
        ),
        migrations.AlterField(
            model_name='salidaterreno',
            name='diasemana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coordinador.diasemana'),
        ),
        migrations.AlterField(
            model_name='salidaterreno',
            name='docente_titular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salidas_terreno_titular', to='core.usersmetadata'),
        ),
        migrations.RemoveField(
            model_name='salidaterreno',
            name='docentes_apoyo',
        ),
        migrations.AlterField(
            model_name='salidaterreno',
            name='semestre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='salidaterreno',
            name='actividad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coordinador.actividad'),
        ),
        migrations.AddField(
            model_name='salidaterreno',
            name='docentes_apoyo',
            field=models.ManyToManyField(blank=True, null=True, related_name='salidas_terreno_apoyo', to='core.usersmetadata'),
        ),
    ]

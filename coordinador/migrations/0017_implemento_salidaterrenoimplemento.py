# Generated by Django 4.2 on 2024-02-22 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0016_pronosticoclima_ultima_actualizacion_api'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('requerido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SalidaTerrenoImplemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presente', models.BooleanField(default=False)),
                ('implemento', models.ManyToManyField(blank=True, related_name='salida_terreno_implemento', to='coordinador.implemento')),
                ('salida_terreno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coordinador.salidaterreno')),
            ],
        ),
    ]
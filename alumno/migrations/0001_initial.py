# Generated by Django 4.2 on 2024-01-31 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_remove_usersmetadata_region_comuna_region_and_more'),
        ('coordinador', '0009_remove_salidaterreno_dias_actividad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Documento_inasis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='alumno.estado')),
                ('salida_terreno', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coordinador.salidaterreno')),
                ('users_metadata', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='documentos', to='core.usersmetadata')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2024-04-03 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0026_alter_documentosterreno_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salidaterreno',
            name='documentos',
        ),
        migrations.AddField(
            model_name='documentosterreno',
            name='salida_terreno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='coordinador.salidaterreno'),
        ),
    ]

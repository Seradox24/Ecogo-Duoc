# Generated by Django 4.2 on 2024-02-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0015_currentclima'),
    ]

    operations = [
        migrations.AddField(
            model_name='pronosticoclima',
            name='ultima_actualizacion_api',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

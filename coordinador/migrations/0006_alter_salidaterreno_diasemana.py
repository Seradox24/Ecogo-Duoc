# Generated by Django 4.2 on 2024-01-17 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0005_salidaterreno_semana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidaterreno',
            name='diasemana',
            field=models.ManyToManyField(blank=True, to='coordinador.diasemana'),
        ),
    ]
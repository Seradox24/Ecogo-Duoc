# Generated by Django 4.2 on 2024-04-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0024_documentosterreno_salidaterreno_documentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidaterreno',
            name='documentos',
            field=models.ManyToManyField(blank=True, to='coordinador.documentosterreno'),
        ),
    ]
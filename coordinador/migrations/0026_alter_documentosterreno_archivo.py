# Generated by Django 4.2 on 2024-04-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0025_alter_salidaterreno_documentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentosterreno',
            name='archivo',
            field=models.FileField(upload_to='documentos/salidas/'),
        ),
    ]

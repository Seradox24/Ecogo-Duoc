# Generated by Django 4.2 on 2024-01-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador', '0007_alter_salidaterreno_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidaterreno',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

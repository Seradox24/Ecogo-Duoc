# Generated by Django 4.2 on 2024-03-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_seccion_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='usuarios',
            field=models.ManyToManyField(blank=True, related_name='secciones', to='core.usersmetadata'),
        ),
    ]
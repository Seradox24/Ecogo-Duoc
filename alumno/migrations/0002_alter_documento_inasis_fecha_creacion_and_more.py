# Generated by Django 4.2 on 2024-01-31 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_usersmetadata_region_comuna_region_and_more'),
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento_inasis',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='documento_inasis',
            name='users_metadata',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='documentos', to='core.usersmetadata'),
        ),
    ]

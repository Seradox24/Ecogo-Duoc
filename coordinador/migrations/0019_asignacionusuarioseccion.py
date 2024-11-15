# Generated by Django 4.2 on 2024-03-12 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_remove_asignatura_docentes'),
        ('coordinador', '0018_remove_salidaterreno_asignatura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionUsuarioSeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.asignatura')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.seccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Asignación Usuario Sección',
                'verbose_name_plural': 'Asignaciones Usuarios Secciones',
            },
        ),
    ]

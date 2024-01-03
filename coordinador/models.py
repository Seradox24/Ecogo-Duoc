from django.db import models

# Create your models here.

class SalidaTerreno(models.Model):
    SITUACION_CHOICES = [
        (1, 'Ejecutado'),
        (2, 'Por Ejecutar'),
    ]

    SEMESTRE_CHOICES = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
    ]

    ACTIVIDAD_CHOICES = [
        (1, 'Interpretación de comunidades (TTO Experiencias)'),
        (2, 'Técnicas Invernales'),
        (3, 'Cabalgata'),
        (4, 'Caracterización de la unidad'),
        (5, 'Análisis de riesgo'),
        (6, 'Valorización del entorno, servicios ecosistémicos y capital humano'),
        (7, 'Interpretación'),
        (8, 'Buceo'),
        (9, 'MTB y KAYAK'),
        (10, 'Escalada'),
        (11, 'MTB'),
        (12, 'KAYAK'),
        (13, 'Terreno Fauna'),
        (14, 'Normativas y procesos, programacion de actividades'),
        (15, 'Trekking'),
        (16, 'Examen Transversal'),
        (17, 'Por Definir'),

    ]

    ASIGNATURA_CHOICES = [
        (1, 'Taller de Integración de Comunidades en Ecoturismo'),
        (2, 'Taller de Actividades al Aire Libre II'),
        (3, 'Taller de Actividades al Aire Libre IV'),
        (4, 'Planificación y Logística de Programas Ecoturísticos'),
        (5, 'Administración Turística de Áreas Protegidas'),
        (6, 'Taller de Gestión de Riesgos en Zonas Remotas'),
        (7, 'Taller de Integración de Ecoturismo en Áreas Silvestres'),
        (8, 'Técnicas de Guiado e interpretación del patrimonio natural'),
        (9, 'Taller Básico de Primeros Auxilios en Áreas Silvestres'),
        (10, 'FAUNA DE CHILE'),
        (11, 'FLORA DE CHILE'),
        (12, 'Taller de Operaciones de Programas de Ecoturismo'),
    ]

    EXP_APRENDIZAJE_CHOICES = [
        (1, 'EA 1'),
        (2, 'EA 2'),
        (3, 'EA 3'),
        (4, 'EA 4'),
        (5, 'EA 5'),
        (6, 'EA 6'),
        (6, 'Examen Transversal'),
        (7, 'Por Definir'),
        
    ]

    SECCION_DOCENTE_CHOISES = [
        (1, '001-D'),
        (2, '002-D'),
        (3, '003-D'),
        (4, '005-D'),
        (5, '001-D / 003-D'),
        (6, '002-D / 004-D'),
        (7, '001-D / 002-D / 003-D'),
        (8, '001-D / 003-D / 005-D'),
        (9, 'Por Definir'),
    ]

    DOCENTE_TITULAR_CHOISES = [
        (1, 'Cristián Thorsoe'),
        (2, 'Matías Sierra'),
        (3, 'Valentina Vergara'),
        (4, 'Hernán Castillo'),
        (5, 'Ramón Andrade'),
        (6, 'Fernando Retamal'),
        (7, 'Marcela Cerda'),
        (8, 'Christian Guntert'),
        (9, 'Victoria Leiva'),
        (10, 'No se requiere'),
    ]

    ASIG_COMP_TERRENO_CHOISES = [
        (1, 'Taller de Actividades al Aire Libre II'),
        (2, 'Taller de Actividades al Aire Libre IV'),
        (3, 'Planificación y Logística de Programas Ecoturísticos'),
        (4, 'Taller de Gestión de Riesgos en Zonas Remotas / Taller de Integración de Ecoturismo en Áreas Silvestres'),
        (5, 'Administración Turística de Áreas Protegidas / Taller de Integración de Ecoturismo en Áreas Silvestres'),
        (6, 'Administración Turística de Áreas Protegidas / Taller de Gestión de Riesgos en Zonas Remotas'),
        (7, 'Taller Básico de Primeros Auxilios en Áreas Silvestres / Taller de Actividades al Aire Libre II'),
        (8, 'Técnicas de Guiado e interpretación del patrimonio natural / Taller Básico de Primeros Auxilios en Áreas Silvestres'),
        (9, 'Taller de Actividades al Aire Libre II / Técnicas de Guiado e interpretación del patrimonio natural'),
        (10, 'No Comparte'),
    ]

    situacion = models.IntegerField(choices=SITUACION_CHOICES, default=1)
    numero_cuenta = models.TextField()
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES, default=1)
    anio = models.TextField()
    semana = models.TextField()
    actividad = models.IntegerField(choices=ACTIVIDAD_CHOICES, default=1)
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()
    dias = models.TextField()
    noches = models.TextField()
    dias_actividad = models.TextField()
    lugar_ejecucion = models.TextField()
    asignatura = models.IntegerField(choices=ASIGNATURA_CHOICES, default=1)
    exp_aprendizaje = models.IntegerField(choices=EXP_APRENDIZAJE_CHOICES, default=1)
    num_alumnos = models.IntegerField()
    seccion_docente = models.IntegerField(choices=SECCION_DOCENTE_CHOISES, default=1)
    docente_titular = models.IntegerField(choices=DOCENTE_TITULAR_CHOISES, default=1)
    docentes_apoyo = models.TextField()
    num_salida = models.IntegerField()
    asig_comp_terreno = models.IntegerField(choices=ASIG_COMP_TERRENO_CHOISES, default=1)
    observaciones = models.TextField()

    def __str__(self):
        return f"Salida Terreno - {self.id}"


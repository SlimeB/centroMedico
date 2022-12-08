# Generated by Django 4.1.2 on 2022-12-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMedica', '0003_boleta_alter_cita_duracioncita_alter_cita_fechacita_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Boleta',
        ),
        migrations.AlterField(
            model_name='cita',
            name='duracionCita',
            field=models.IntegerField(default=0, verbose_name='duracion aproximada de la cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='horaInicioCita',
            field=models.TimeField(default=0, verbose_name='hora de la cita'),
        ),
    ]
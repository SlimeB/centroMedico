# Generated by Django 4.1.2 on 2022-11-24 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMedica', '0002_perfil_cita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCitaBoleta', models.IntegerField()),
                ('fechaEmisionBoleta', models.DateTimeField(auto_now_add=True)),
                ('valorBrutoBoleta', models.IntegerField()),
                ('valorNetoBoleta', models.IntegerField()),
                ('comisionMedicaBoleta', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='cita',
            name='duracionCita',
            field=models.IntegerField(choices=[('0', 'seleccione una opción'), ('1', '15 minutos'), ('2', '30 minutos'), ('3', '45 minutos'), ('4', '60 minutos')], default=0, verbose_name='duracion aproximada de la cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fechaCita',
            field=models.DateTimeField(verbose_name='fecha de la cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='horaInicioCita',
            field=models.TimeField(choices=[('0', 'seleccione una opción'), ('1', '0:00'), ('2', '1:00'), ('3', '2:00'), ('4', '3:00'), ('5', '4:00'), ('6', '5:00'), ('7', '6:00'), ('8', '7:00'), ('9', '8:00'), ('10', '9:00'), ('11', '10:00'), ('12', '11:00'), ('13', '12:00'), ('14', '13:00'), ('15', '14:00'), ('16', '15:00'), ('17', '16:00'), ('18', '17:00'), ('19', '18:00'), ('20', '19:00'), ('21', '20:00'), ('22', '21:00'), ('23', '22:00'), ('24', '23:00')], default=0, verbose_name='hora de la cita'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='especialidadUsuario',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appMedica.especialidad', verbose_name='especialidad del medico'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rolUsuario',
            field=models.ForeignKey(default='Paciente', on_delete=django.db.models.deletion.DO_NOTHING, to='appMedica.rol', verbose_name='rol del usuario'),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('rutUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='rut(sin digito verificador)')),
                ('dvUsuario', models.CharField(max_length=1, verbose_name='digito verificador')),
                ('nombreUsuario', models.CharField(max_length=30, verbose_name='nombre')),
                ('apellidoUsuario', models.CharField(max_length=30, verbose_name='apellido')),
                ('direccionUsuario', models.CharField(max_length=40, verbose_name='dirrecion')),
                ('telefonoUsuario', models.CharField(max_length=12, verbose_name='telefono celular')),
                ('mailUsuario', models.EmailField(max_length=40, verbose_name='email')),
                ('especialidadUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='appMedica.especialidad', verbose_name='especialidad del medico')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='cita',
            name='medicoCita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='medicoCita', to='appMedica.medico', verbose_name='médico para la cita'),
        ),
    ]

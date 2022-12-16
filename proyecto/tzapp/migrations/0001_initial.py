# Generated by Django 4.1.3 on 2022-12-15 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCamionRecepcionLeche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('numero_guia', models.IntegerField()),
                ('sello', models.CharField(max_length=100)),
                ('temperatura_leche_guia', models.FloatField()),
                ('temperatura_leche_pool', models.FloatField()),
                ('temperatura_leche_salida_enfriador', models.FloatField()),
                ('litros_camion', models.FloatField()),
                ('kilo_gramos_camion', models.FloatField()),
                ('litros_sap', models.IntegerField()),
                ('acidez', models.FloatField()),
                ('ph_camion', models.FloatField()),
                ('prueba', models.FloatField()),
                ('snap', models.CharField(max_length=20)),
                ('mg', models.FloatField()),
                ('sng', models.FloatField()),
                ('st', models.FloatField()),
                ('proteina', models.FloatField()),
                ('densidad', models.FloatField()),
                ('color_y_olor', models.CharField(max_length=30)),
                ('hora_ingreso_a_planta', models.TimeField()),
                ('hora_muestra', models.TimeField()),
                ('hora_inicio_descarga', models.TimeField()),
                ('hora_termino_descarga', models.TimeField()),
                ('hora_inicio_aseo', models.TimeField()),
                ('hora_termino_aseo', models.TimeField()),
                ('hora_salida_planta', models.TimeField()),
                ('kilo_gramos_camion_salida', models.FloatField()),
                ('tipo_aseo_camion', models.CharField(max_length=30)),
                ('comentario', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tlp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleTlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_y_hora_estandarizacion', models.DateTimeField(auto_now_add=True)),
                ('detalle_camion_recepcion_leche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detallecamionrecepcionleche')),
                ('tlc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tlc')),
            ],
        ),
        migrations.AddField(
            model_name='detallecamionrecepcionleche',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.operador'),
        ),
        migrations.AddField(
            model_name='detallecamionrecepcionleche',
            name='placa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.camion'),
        ),
        migrations.AddField(
            model_name='detallecamionrecepcionleche',
            name='recorrido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.recorrido'),
        ),
        migrations.AddField(
            model_name='detallecamionrecepcionleche',
            name='tlc',
            field=models.ManyToManyField(through='tzapp.DetalleTlc', to='tzapp.tlc'),
        ),
        migrations.CreateModel(
            name='Detalle_pasteurizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField()),
                ('litros_salida_tlp', models.IntegerField()),
                ('saldo', models.IntegerField()),
                ('tipo_leche', models.CharField(max_length=30)),
                ('observacion', models.CharField(max_length=30)),
                ('fecha_pasteurizacion', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_termino', models.TimeField()),
                ('temperatura_salida_pasteurizador', models.FloatField()),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.operador')),
                ('tct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tct')),
                ('tlc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalletlc')),
                ('tlp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tlp')),
            ],
        ),
    ]

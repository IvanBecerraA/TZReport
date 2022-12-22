# Generated by Django 4.1.3 on 2022-12-21 22:53

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
                ('comentario', models.CharField(max_length=100, null=True)),
                ('usuario_del_registro', models.CharField(max_length=100, null=True)),
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
                ('usuario_del_registro', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleInsumosEnvasado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleInsumosFormulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_fabricacion', models.DateField()),
                ('hora_fabricacion', models.TimeField()),
                ('fecha_formulacion', models.DateField()),
                ('hora_formulacion', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleTlp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('detalle_pasteurizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalle_pasteurizacion')),
            ],
        ),
        migrations.CreateModel(
            name='EstanqueFermentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstanqueLanzamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
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
            name='parametrosRepo001',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura_leche_guia_minimo', models.FloatField()),
                ('temperatura_leche_guia_maximo', models.FloatField()),
                ('temperatura_leche_pool_minimo', models.FloatField()),
                ('temperatura_leche_pool_maximo', models.FloatField()),
                ('temperatura_leche_salida_enfriador_minimo', models.FloatField()),
                ('temperatura_leche_salida_enfriador_maximo', models.FloatField()),
                ('acidez_minimo', models.FloatField()),
                ('acidez_maximo', models.FloatField()),
                ('ph_camion_minimo', models.FloatField()),
                ('ph_camion_maximo', models.FloatField()),
                ('prueba_minimo', models.FloatField()),
                ('prueba_maximo', models.FloatField()),
                ('mg_minimo', models.FloatField()),
                ('mg_maximo', models.FloatField()),
                ('sng_minimo', models.FloatField()),
                ('sng_maximo', models.FloatField()),
                ('st_minimo', models.FloatField()),
                ('st_maximo', models.FloatField()),
                ('proteina_minimo', models.FloatField()),
                ('proteina_maximo', models.FloatField()),
                ('densidad_minimo', models.FloatField()),
                ('densidad_maximo', models.FloatField()),
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
            name='Tmy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenProceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_proceso', models.IntegerField()),
                ('orden_proceso_base_blanca', models.IntegerField()),
                ('producto', models.CharField(max_length=50, null=True)),
                ('sabor', models.CharField(max_length=50, null=True)),
                ('litros', models.FloatField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('operador_pasteurizacion', models.CharField(max_length=50, null=True)),
                ('operador_fermentacion', models.CharField(max_length=50, null=True)),
                ('operador_dosimetria', models.CharField(max_length=50, null=True)),
                ('cantidad_tlp', models.FloatField()),
                ('cantidad_crema', models.FloatField()),
                ('litros_agua', models.FloatField()),
                ('litros_total_llenado', models.FloatField()),
                ('comentario', models.CharField(max_length=100, null=True)),
                ('usuario_del_registro', models.CharField(max_length=100, null=True)),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.maquina')),
                ('tct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tct')),
                ('tlp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalletlp')),
                ('tmy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tmy')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrimaEnvasado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('kilos_consumo', models.IntegerField()),
                ('lote', models.CharField(max_length=50)),
                ('numero_contenedor', models.IntegerField()),
                ('numero_usos', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('hora_uso', models.TimeField()),
                ('detalle_insumo_envasado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalleinsumosenvasado')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('kilos', models.IntegerField()),
                ('lote', models.CharField(max_length=50)),
                ('fecha_vencimiento', models.DateField()),
                ('detalle_pasteurizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalleinsumosformulacion')),
            ],
        ),
        migrations.AddField(
            model_name='detalletlp',
            name='tlp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tlp'),
        ),
        migrations.CreateModel(
            name='DetalleTlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('detalle_camion_recepcion_leche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detallecamionrecepcionleche')),
                ('tlc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tlc')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleRepo068',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_estandarizacion', models.DateField()),
                ('hora_estandarizacion', models.TimeField()),
                ('acidez_leche', models.FloatField()),
                ('temperatura_leche', models.FloatField()),
                ('materia_grasa_leche', models.FloatField()),
                ('densidad_leche', models.FloatField()),
                ('proteina_leche', models.FloatField()),
                ('operador_muestra_leche', models.CharField(max_length=50)),
                ('acidez_mezcla', models.FloatField()),
                ('temperatura_mezcla', models.FloatField()),
                ('materia_grasa_mezcla', models.FloatField()),
                ('densidad_mezcla', models.FloatField()),
                ('solidos_totales_mezcla', models.FloatField()),
                ('operador_muestra_mezcla', models.CharField(max_length=50)),
                ('filtro_pasteurizador', models.CharField(max_length=20)),
                ('filtro_311', models.CharField(max_length=20)),
                ('filtro_312', models.CharField(max_length=20)),
                ('filtro_313', models.CharField(max_length=20)),
                ('filtro_314', models.CharField(max_length=20)),
                ('filtro_316', models.CharField(max_length=20)),
                ('hora_inicio_pasteurizacion', models.TimeField()),
                ('hora_adicion_fermentos', models.TimeField()),
                ('fermento', models.CharField(max_length=50)),
                ('fermento_lote', models.CharField(max_length=50)),
                ('temperatura_pasteurizador', models.FloatField()),
                ('presion_pasteurizador', models.FloatField()),
                ('hora_termino_pasteurizacion', models.TimeField()),
                ('litros_pasteurizados', models.FloatField()),
                ('ph_corte', models.FloatField()),
                ('tiempo_fermentacion', models.TimeField()),
                ('inicio_enfriamiento', models.TimeField()),
                ('termino_enfriamiento', models.TimeField()),
                ('tiempo_enfriamiento', models.TimeField()),
                ('presion_enfriamiento', models.FloatField()),
                ('ystral_enfriamiento', models.IntegerField()),
                ('viscosidad', models.IntegerField()),
                ('grumos', models.CharField(max_length=10)),
                ('espuma', models.CharField(max_length=10)),
                ('desuerado', models.CharField(max_length=10)),
                ('sabor', models.CharField(max_length=10)),
                ('temperatura_frio', models.FloatField()),
                ('comentario', models.CharField(max_length=100, null=True)),
                ('usuario_del_registro', models.CharField(max_length=100, null=True)),
                ('estanque_fermentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.estanquefermentacion')),
                ('estanque_lanzamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.estanquelanzamiento')),
                ('orden_proceso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tzapp.ordenproceso')),
            ],
        ),
        migrations.AddField(
            model_name='detalleinsumosformulacion',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.operador'),
        ),
        migrations.AddField(
            model_name='detalleinsumosformulacion',
            name='orden_proceso',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tzapp.ordenproceso'),
        ),
        migrations.AddField(
            model_name='detalleinsumosenvasado',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.operador'),
        ),
        migrations.AddField(
            model_name='detalleinsumosenvasado',
            name='orden_proceso',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tzapp.ordenproceso'),
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
        migrations.AddField(
            model_name='detalle_pasteurizacion',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.operador'),
        ),
        migrations.AddField(
            model_name='detalle_pasteurizacion',
            name='tct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tct'),
        ),
        migrations.AddField(
            model_name='detalle_pasteurizacion',
            name='tlc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalletlc'),
        ),
        migrations.AddField(
            model_name='detalle_pasteurizacion',
            name='tlp',
            field=models.ManyToManyField(through='tzapp.DetalleTlp', to='tzapp.tlp'),
        ),
    ]

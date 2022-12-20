# Generated by Django 4.1.3 on 2022-12-20 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tzapp', '0004_detallecamionrecepcionleche_usuario_del_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tmy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='detalle_pasteurizacion',
            name='comentario',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detalle_pasteurizacion',
            name='usuario_del_registro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='OrdenProceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_proceso_base_blanca', models.IntegerField()),
                ('orden_Proceso', models.IntegerField()),
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
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.sabor')),
                ('tct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tct')),
                ('tlp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.detalletlp')),
                ('tmy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tzapp.tmy')),
            ],
        ),
    ]

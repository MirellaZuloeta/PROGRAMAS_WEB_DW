# Generated by Django 3.2 on 2021-10-30 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('tipoDocID', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigoCli', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('nomUsuario', models.CharField(max_length=30, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('numeroDocumento', models.CharField(max_length=21, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clientes')),
                ('tipoDocID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='administrador.tipodocumento')),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=100)),
                ('duracion', models.DecimalField(decimal_places=1, max_digits=2)),
                ('facultad', models.CharField(max_length=40)),
                ('cantidad_materias', models.IntegerField(verbose_name='Materias')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('carrera', models.CharField(max_length=40)),
                ('edad', models.PositiveIntegerField()),
                ('dni', models.PositiveBigIntegerField(verbose_name='DNI')),
                ('legajo', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('catedra', models.CharField(max_length=40)),
                ('materia_dictada', models.CharField(max_length=50)),
                ('edad', models.PositiveIntegerField()),
                ('dni', models.PositiveBigIntegerField(verbose_name='DNI')),
            ],
        ),
    ]
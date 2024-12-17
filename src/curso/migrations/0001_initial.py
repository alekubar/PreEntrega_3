# Generated by Django 5.1.4 on 2024-12-17 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('fecha_inicio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('comision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curso.comision')),
            ],
        ),
        migrations.AddField(
            model_name='comision',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curso.curso'),
        ),
    ]
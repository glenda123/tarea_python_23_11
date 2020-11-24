# Generated by Django 2.2.14 on 2020-11-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, null=True)),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.IntegerField(null=True)),
                ('direccion', models.CharField(max_length=300)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('clase', models.ManyToManyField(related_name='estudiantes', to='clases.Clase')),
            ],
        ),
    ]

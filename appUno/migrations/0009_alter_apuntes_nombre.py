# Generated by Django 4.1.2 on 2022-11-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUno', '0008_alter_apuntes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apuntes',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre de la nota'),
        ),
    ]

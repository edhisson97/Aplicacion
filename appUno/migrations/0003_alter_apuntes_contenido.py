# Generated by Django 4.1.2 on 2022-10-31 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUno', '0002_apuntes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apuntes',
            name='contenido',
            field=models.CharField(max_length=30),
        ),
    ]
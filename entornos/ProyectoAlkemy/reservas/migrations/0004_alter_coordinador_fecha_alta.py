# Generated by Django 4.2.1 on 2023-06-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_reservaservicio_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinador',
            name='fecha_alta',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta'),
        ),
    ]

# Generated by Django 3.0 on 2019-12-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('malquileres', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alquiler',
            name='cliente',
        ),
    ]

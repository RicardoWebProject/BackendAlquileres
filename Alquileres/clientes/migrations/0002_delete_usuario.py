# Generated by Django 3.0 on 2019-12-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('malquileres', '0002_remove_alquiler_cliente'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]

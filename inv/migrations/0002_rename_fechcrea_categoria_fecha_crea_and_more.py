# Generated by Django 4.0 on 2021-12-14 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='fechCrea',
            new_name='fecha_crea',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='fechModif',
            new_name='fecha_modifica',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='usrCrea',
            new_name='usuario_crea',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='usrModif',
            new_name='usuario_modifica',
        ),
    ]
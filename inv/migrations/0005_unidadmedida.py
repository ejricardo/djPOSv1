# Generated by Django 4.0 on 2021-12-19 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('inv', '0004_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_crea', models.DateTimeField(auto_now_add=True)),
                ('usuario_modifica', models.IntegerField(blank=True, null=True)),
                ('fecha_modifica', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(help_text='Descripción de la unidad de medida', max_length=100, unique=True)),
                ('usuario_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Unidades de medida',
            },
        ),
    ]

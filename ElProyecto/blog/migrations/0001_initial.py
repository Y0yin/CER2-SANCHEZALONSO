# Generated by Django 4.2.6 on 2023-10-22 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('detalle', models.CharField(max_length=150)),
                ('detalle_corto', models.CharField(max_length=60)),
                ('tipo', models.CharField(choices=[('S', 'Suspensión de actividades'), ('C', 'Suspensión de clase'), ('I', 'Información')], max_length=100)),
                ('visible', models.BooleanField(default=False)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificación', models.DateTimeField(auto_now=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.entidad')),
                ('modificado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunicado_modificado', to=settings.AUTH_USER_MODEL)),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunicado_publicado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

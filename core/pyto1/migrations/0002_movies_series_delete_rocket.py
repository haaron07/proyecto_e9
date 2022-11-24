# Generated by Django 4.1.3 on 2022-11-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyto1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='repositorio/proyecto2/fotos', verbose_name='Image')),
                ('video', models.FileField(blank=True, null=True, upload_to='repositorio/proyecto2/videos', verbose_name='Media')),
                ('description', models.TextField(max_length=255, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='repositorio/proyecto1/fotos', verbose_name='Image')),
                ('video', models.FileField(blank=True, null=True, upload_to='repositorio/proyecto1/videos', verbose_name='Media')),
                ('description', models.TextField(max_length=255, verbose_name='Descripcion')),
            ],
        ),
        migrations.DeleteModel(
            name='Rocket',
        ),
    ]

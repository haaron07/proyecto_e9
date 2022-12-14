# Generated by Django 4.1.3 on 2022-11-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyto1', '0002_movies_series_delete_rocket'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGames',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='repositorio/proyecto3/fotos', verbose_name='Image')),
                ('video', models.FileField(blank=True, null=True, upload_to='repositorio/proyecto3/videos', verbose_name='Media')),
                ('description', models.TextField(max_length=255, verbose_name='Descripcion')),
            ],
        ),
    ]

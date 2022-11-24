from django.db import models

# Create your models here.
class Series(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen=models.ImageField(upload_to='proyecto1/fotos',null=True,blank=True, verbose_name='Image')
    video=models.FileField(upload_to='proyecto1/videos',null=True,blank=True, verbose_name='Media')
    description=models.TextField(max_length=255, verbose_name='Descripcion')
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.description
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        self.video.storage.delete(self.video.name)
        super().delete()

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen=models.ImageField(upload_to='proyecto2/fotos',null=True,blank=True, verbose_name='Image')
    video=models.FileField(upload_to='proyecto2/videos',null=True,blank=True, verbose_name='Media')
    description=models.TextField(max_length=255, verbose_name='Descripcion')
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.description
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        self.video.storage.delete(self.video.name)
        super().delete()

class VideoGames(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen=models.ImageField(upload_to='proyecto3/fotos',null=True,blank=True, verbose_name='Image')
    video=models.FileField(upload_to='proyecto3/videos',null=True,blank=True, verbose_name='Media')
    description=models.TextField(max_length=255, verbose_name='Descripcion')
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.description
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        self.video.storage.delete(self.video.name)
        super().delete()

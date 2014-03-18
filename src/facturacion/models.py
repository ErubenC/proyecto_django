from django.db import models


class Marca(models.Model):
    nombre  =   models.CharField(max_length=50)
    codigo_propio   =   models.CharField(max_length=50)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre
    
class GrupoItem(models.Model):
    nombre  =   models.CharField(max_length=50)
    codigo_propio   =   models.CharField(max_length=50)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre
    
class Unidad(models.Model):
    nombre = models.CharField(max_length=30)
    codigo_propio   =   models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre
    
class Bodega(models.Model):
    nombre  = models.CharField(max_length=50)
    codigo_propio   =   models.CharField(max_length=50)
    direccion   = models.CharField(max_length=50)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre

class Item(models.Model):
    codigo_barras   = models.CharField(max_length=50)
    codigo_propio   = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=200)
    es_bien         = models.BooleanField(default=False)
    es_servicio     = models.BooleanField(default=False)
    iva             = models.BooleanField(default=False)
    ubicacion       = models.CharField(max_length=300)
    id_marca        = models.ForeignKey(Marca)
    id_grupo        = models.ForeignKey(GrupoItem)
    id_unidad       = models.ForeignKey(Unidad)
    item_bodega     = models.ManyToManyField(Bodega)
    
    

   
    

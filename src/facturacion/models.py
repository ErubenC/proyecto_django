from django.db import models

'''
Estas clases pertenecen al modelo para agregar marcas, bodegas, grupos e items
'''

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
    
    def __str__(self):              # __unicode__ on Python 2
        return self.descripcion


'''
Estas clases pertenecen al modelo para agregar proveedores y clientes
tambien estan incluidas las tablas que contiene las ciudades y las provincias
'''
    
class Provincia(models.Model):
    nombre = models.CharField(max_length=40)
    codigo_propio   = models.CharField(max_length=30)
    
class Canton(models.Model):
    nombre = models.CharField(max_length=40)
    codigo_propio   = models.CharField(max_length=30)
    provincia       = models.ForeignKey(Provincia)

class Proveedor(models.Model):
    nombre_comercial = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    codigo_propio   = models.CharField(max_length=30)
    #usamos un bigInteger ya que el numero de RUC tiene 12 digitos
    ruc = models.BigIntegerField()
    direccion = models.CharField(max_length=200)
    mail = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    canton = models.ForeignKey(Canton)
    
class Cliente(models.Model):
    nombre_comercial = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    codigo_propio   = models.CharField(max_length=30)
    #usamos un bigInteger ya que el numero de RUC tiene 12 digitos
    ruc = models.BigIntegerField()
    direccion = models.CharField(max_length=200)
    mail = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    canton = models.ForeignKey(Canton)
    

    

    
    
      
    

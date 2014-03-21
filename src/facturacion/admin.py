from django.contrib import admin
from models import Marca,GrupoItem,Unidad,Bodega,Item
from facturacion.models import Proveedor, Cliente, Canton, Provincia, Grupo_doc, Transaccion, \
Rubro_cancelacion, Documento

admin.site.register(Marca)
admin.site.register(GrupoItem)
admin.site.register(Unidad)
admin.site.register(Bodega)
admin.site.register(Item)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Canton)
admin.site.register(Provincia)
admin.site.register(Grupo_doc)
admin.site.register(Transaccion)
admin.site.register(Rubro_cancelacion)
admin.site.register(Documento)

# Register your models here.

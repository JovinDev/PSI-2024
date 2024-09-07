from django.contrib import admin #isso já vai estar existindo no arquivo
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)


from django.contrib import admin #isso já vai estar existindo no arquivo
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):

# Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
        date_hierarchy = 'criado_em'
        list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao','preco', 'categoria',)
        empty_value_display = 'Vazio'
        fields = ('Produto', 'destaque', 'promocao','msgPromocao', 'preco', 'categoria',)
        exclude = ('msgPromocao',)

admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)


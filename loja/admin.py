from django.contrib import admin #isso já vai estar existindo no arquivo
# Register your models here.
from .models import *
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)
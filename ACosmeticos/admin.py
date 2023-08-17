from django.contrib import admin

# Register your models here.

from django.contrib import admin

from ACosmeticos.models import Cliente, Carrinho, Marcas, Produto, ItemCarrinho, Favorito, FormaPagamento

admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(Marcas)
admin.site.register(Produto)
admin.site.register(ItemCarrinho)
admin.site.register(Favorito)
admin.site.register(FormaPagamento)
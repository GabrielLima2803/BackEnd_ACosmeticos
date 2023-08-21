from django.contrib import admin

# Register your models here.

from django.contrib import admin

from ACosmeticos.models import Cliente, Carrinho, Marca, Produto, ItemCarrinho, Favorito, FormaPagamento, Compra

admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(ItemCarrinho)
admin.site.register(Favorito)
admin.site.register(FormaPagamento)


class ItensInline(admin.TabularInline):
    model = ItemCarrinho

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)




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

admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Gerenciamento de clientes.

    Exibe os seguintes campos na lista:
        nome: O nome do cliente.
        email: O endereço de e-mail do cliente.

    Filtra os resultados pela coluna `nome`.

    Ordena os resultados pelas colunas `nome` e `email`.
    """

    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')
    search_fields = ('nome', 'marca__descricao')
    list_filter = ('marca',)
    ordering = ('nome', 'marca')
    list_per_page = 25



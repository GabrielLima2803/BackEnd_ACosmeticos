from django.contrib import admin
from django.urls import include, path
from django.urls import path

from rest_framework.routers import DefaultRouter

from ACosmeticos.views import ProdutoViewSet, MarcasViewSet, CarrinhoViewSet, FavoritoViewSet, ClienteViewSet, ItemCarrinhoViewSet, FormaPagamentoViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet)
router.register(r"marcas", MarcasViewSet)
router.register(r"carrinho", CarrinhoViewSet)
router.register(r"itemcarrinho", ItemCarrinhoViewSet)
router.register(r"favorito", FavoritoViewSet)
router.register(r"cliente", ClienteViewSet)
router.register(r"formaPagamento", FormaPagamentoViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]





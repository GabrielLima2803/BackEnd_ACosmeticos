from django.contrib import admin
from django.urls import include, path
from django.urls import path

from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from ACosmeticos.views import ProdutoViewSet, MarcasViewSet, CarrinhoViewSet, FavoritoViewSet, ClienteViewSet, ItemCarrinhoViewSet, FormaPagamentoViewSet, CompraViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet)
router.register(r"marcas", MarcasViewSet)
router.register(r"carrinho", CarrinhoViewSet)
router.register(r"itemcarrinho", ItemCarrinhoViewSet)
router.register(r"favorito", FavoritoViewSet)
router.register(r"cliente", ClienteViewSet)
router.register(r"formaPagamento", FormaPagamentoViewSet)
router.register(r"compras", CompraViewSet)


urlpatterns = [
    path("apiU/", include(usuario_router.urls)),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

] + static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)





from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from ACosmeticos.views import ProdutoViewSet, MarcasViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet)
router.register(r"marcas", MarcasViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]


from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from ACosmeticos.models import Produto, Marcas
from ACosmeticos.serializers import ProdutoSerializer, MarcasSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class MarcasViewSet(ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer





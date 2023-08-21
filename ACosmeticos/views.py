from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from rest_framework.permissions import IsAuthenticated


# from rest_framework.permissions import IsAuthenticated

from ACosmeticos.models import Produto, Marcas, ItemCarrinho, Favorito, Carrinho, Cliente, FormaPagamento
from ACosmeticos.serializers import ProdutoSerializer, MarcasSerializer, ItemCarrinhoSerializer, FavoritoSerializer, CarrinhoSerializer, ClienteSerializer, FormaPagamentoSerializer 

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # permission_classes = [IsAuthenticated]

class MarcasViewSet(ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer
    # permission_classes = [IsAuthenticated]

class ItemCarrinhoViewSet(ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer

class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FormaPagamentoViewSet(ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

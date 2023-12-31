from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated


# from rest_framework.permissions import IsAuthenticated

from ACosmeticos.models import Produto, Marca, ItemCarrinho, Favorito, Carrinho, Cliente, FormaPagamento
from ACosmeticos.serializers import ( 
    ProdutoSerializer, 
    MarcasSerializer, 
    FavoritoSerializer, 
    CarrinhoListSerializer, 
    CarrinhoCreateSerializer,
    ClienteSerializer, 
    FormaPagamentoSerializer, 
    UsuarioSerializer
)

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class MarcasViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcasSerializer

# class ItemCarrinhoViewSet(ModelViewSet):
#     queryset = ItemCarrinho.objects.all()
#     serializer_class = ItemCarrinhoSerializer

class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action =='partial_update':
            return CarrinhoCreateSerializer
        return CarrinhoListSerializer
    # serializer_class = CarrinhoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FormaPagamentoViewSet(ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

# class CompraViewSet(ModelViewSet):
#     queryset = Compra.objects.all()
#     def get_queryset(self):
#         usuario = self.request.user
#         if usuario.is_superuser:
#             return Compra.objects.all()
#         if usuario.groups.filter(name="Administradores"):
#             return Compra.objects.all()
#         return Compra.objects.filter(usuario=usuario)
    
#     serializer_class = CompraSerializer
#     def get_serializer_class(self):
#         if self.action == "create" or self.action == "update":
#             return CriarEditarCompraSerializer
#         return CompraSerializer
    

from ACosmeticos.models import Usuario


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
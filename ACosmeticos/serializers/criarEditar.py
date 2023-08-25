from rest_framework.serializers import ModelSerializer, CharField

from ACosmeticos.serializers import ItemCarrinhoSerializer
from ACosmeticos.models import Compra

class CriarEditarCompraSerializer(ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")
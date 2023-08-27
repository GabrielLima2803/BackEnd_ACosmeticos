from rest_framework.serializers import ModelSerializer, CharField

from ACosmeticos.models import Compra
from ACosmeticos.serializers import ItemCarrinhoSerializer

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItemCarrinhoSerializer(many=True, read_only=True)
    status = CharField(source="get_status_display", read_only=True)



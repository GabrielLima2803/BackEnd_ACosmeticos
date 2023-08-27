from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ACosmeticos.models import ItemCarrinho

# Item carrinho
class ItemCarrinhoSerializer(ModelSerializer):
    total = SerializerMethodField()

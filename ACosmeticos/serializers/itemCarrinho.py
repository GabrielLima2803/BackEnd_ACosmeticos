from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import ItemCarrinho

# Item carrinho
class ItemCarrinhoSerializer(ModelSerializer):
    class Meta:
        model = ItemCarrinho
        fields = "__all__"
        depth = 1 
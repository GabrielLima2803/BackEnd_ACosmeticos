from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ACosmeticos.models import ItemCarrinho

# Item carrinho
class ItemCarrinhoSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = ["produto", "quantidade", "total"]
        depth = 2

    def get_total(self, obj):
        return obj.produto.preco * obj.quantidade
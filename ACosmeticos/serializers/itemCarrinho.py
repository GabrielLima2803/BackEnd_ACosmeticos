from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ACosmeticos.models import ItemCarrinho

# Item carrinho
class ItemCarrinhoSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItemCarrinho
        fields = "__all__"
        depth = 1 

total = SerializerMethodField()
def get_total(self, instance):
    return instance.quantidade * instance.produto.preco
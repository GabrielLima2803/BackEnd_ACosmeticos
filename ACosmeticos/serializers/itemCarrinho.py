from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ACosmeticos.models import ItemCarrinho

# Item carrinho
class ItemCarrinhoSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItemCarrinho
        fields = "__all__"
        depth = 1 

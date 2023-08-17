from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Carrinho

# Carrinho
class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"
        depth = 1 
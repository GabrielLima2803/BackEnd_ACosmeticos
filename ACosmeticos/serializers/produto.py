from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Produto

# Produto
class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1        
     
# class ProdutoDetailSerializer(ModelSerializer):
#     class Meta:
#         model = Produto
#         fields = "__all__"
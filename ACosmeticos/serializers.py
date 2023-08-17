from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Produto, Marcas

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

        
class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1        

class MarcasSerializer(ModelSerializer):
    class Meta:
        model = Marcas
        fields = "__all__"
        
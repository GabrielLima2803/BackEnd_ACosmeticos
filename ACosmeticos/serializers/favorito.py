from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Favorito

# Favorito    
class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = "__all__"
        depth = 1 
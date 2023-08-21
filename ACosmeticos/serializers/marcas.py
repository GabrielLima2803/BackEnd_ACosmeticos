from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Marca

# Marcas
class MarcasSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
        depth = 1 
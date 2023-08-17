from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Marcas

# Marcas
class MarcasSerializer(ModelSerializer):
    class Meta:
        model = Marcas
        fields = "__all__"
        depth = 1 
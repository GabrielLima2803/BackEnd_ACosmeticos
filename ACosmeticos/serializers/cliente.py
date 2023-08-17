from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import Cliente

# Cliente
class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        depth = 1 
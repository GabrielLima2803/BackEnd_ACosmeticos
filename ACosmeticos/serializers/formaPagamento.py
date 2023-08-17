from rest_framework.serializers import ModelSerializer

from ACosmeticos.models import FormaPagamento

# Forma de Pagamento
class FormaPagamentoSerializer(ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = "__all__"
        depth = 1 
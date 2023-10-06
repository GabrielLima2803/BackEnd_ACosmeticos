from rest_framework.serializers import ModelSerializer, CharField
from ACosmeticos.models import Compra, ItemCarrinho
from ACosmeticos.serializers import ItemCarrinhoSerializer

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItemCarrinhoSerializer(many=True, read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItemCarrinho.objects.create(compra=instance, **item)
        instance.save()
        return instance


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItemCarrinho
        fields = ("livro", "quantidade")
    def validate(self, data):
        if data["quantidade"] > data["livro"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "Quantidade solicitada não disponível em estoque."}
            )
        return data

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True) # Aqui mudou

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItemCarrinho.objects.create(compra=compra, **item_data)
        compra.save()
        return compra

from rest_framework.serializers import ModelSerializer, CharField

from ACosmeticos.models import Carrinho,  ItemCarrinho


class AddItensCarrinho(ModelSerializer):
    class Meta:
        model = ItemCarrinho
        fields = ('produto', 'quantidade')
   
class ListItensCarrinho(ModelSerializer):    
    produto =  CharField(source="produto.nome")
    class Meta:
        model = ItemCarrinho
        fields = ('produto', 'quantidade')

class CarrinhoListSerializer(ModelSerializer):
    itens = ListItensCarrinho(many=True)
    status = CharField(source='get_status_display')
    class Meta:
        model = Carrinho
        fields = ("status", "cliente", "itens", "total")
        depth = 1 
    
    
class CarrinhoCreateSerializer(ModelSerializer):
    itens = AddItensCarrinho(many=True)
    
    class Meta:
        model = Carrinho
        fields = ("status", "cliente", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        carrinho = Carrinho.objects.create(**validated_data)
        for item_data in itens_data:
            ItemCarrinho.objects.create(carrinho=carrinho, **item_data)
        carrinho.save()
        return carrinho

    def update(self, obj, validated_data):
        obj.itens.all().delete()
        itens_data = validated_data.pop("itens")
        for item_data in itens_data:
            ItemCarrinho.objects.create(carrinho=obj, **item_data)
        # obj.status=
        obj.save()
        return obj
        # breakpoint()
        # itens_data = validated_data.pop("itens")
        
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ACosmeticos.models import Produto
from uploader.models import Image
from uploader.serializers import ImageSerializer


# Produto
class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
        read_only_fields = []

        capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
        )
        capa = ImageSerializer(required=False, read_only=True)       
    
     
class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
    capa = ImageSerializer(required=False)
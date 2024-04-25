from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from endereco.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = [
            'id', 'nome', 'descricao', 'aprovado','endereco',
            'atracoes', 'comentarios', 'avaliacoes',
        ]
        read_only_fields = ('comentarios', )
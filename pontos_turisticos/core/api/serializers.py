from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, Atracao
from atracao.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from endereco.models import Endereco
from avaliacao.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    avaliacoes = AvaliacaoSerializer(read_only=True, many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'descricao_completa',
            'atracoes', 'comentarios', 'avaliacoes', 'endereco',
        )
        read_only_fields = ('comentarios', )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        endereco = validated_data['endereco']
        del validated_data['endereco']

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
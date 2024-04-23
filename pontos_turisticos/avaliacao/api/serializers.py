from ..models import Avaliacao

class AvaliacaoSerializer:
    class Meta:
        model = Avaliacao
        fields = [
            'id', 'usuario', 'comentario', 'nota', 'data'
        ]
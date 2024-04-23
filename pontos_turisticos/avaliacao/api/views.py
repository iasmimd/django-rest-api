from rest_framework.viewsets import ModelViewSet
from ..models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoView(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

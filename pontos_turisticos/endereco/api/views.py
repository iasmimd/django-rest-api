from rest_framework.viewsets import ModelViewSet
from ..models import Endereco
from .serializers import EnderecoSerializer


class EnderecoView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

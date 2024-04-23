from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoView(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    queryset = PontoTuristico.objects.all()

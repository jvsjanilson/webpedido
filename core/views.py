from rest_framework import generics

from core.models import Estado, Cidade
from core.serializers import EstadoSerializer, CidadeSerializer


class EstadosAPIView(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class EstadoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CidadesAPIView(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

    def get_queryset(self):
        if self.kwargs.get('estado_pk'):
            return self.queryset.filter(estado_id=self.kwargs.get('estado_pk'))
        return self.queryset.all()


class CidadeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


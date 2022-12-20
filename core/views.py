from rest_framework import generics

from core.models import Estado, Cidade
from core.serializers import EstadoSerializer, CidadeSerializer

"""
API V1
"""

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


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

"""
API V2
"""

class EstadoViewSet(viewsets.ModelViewSet):
    """
        API V2 Estados
    """
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

    @action(detail=True, methods=['get'])
    def cidades(self, request, pk=None):
        estado = self.get_object()
        serializer = CidadeSerializer(estado.cidades.all(), many=True)
        return Response(serializer.data)


class CidadeViewSet(viewsets.ModelViewSet):
    """
        API V2 Cidades 
    """
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

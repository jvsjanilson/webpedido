from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Estado, Cidade
from core.serializers import EstadoSerializer, CidadeSerializer


class EstadoAPIView(APIView):
    """
        API Estado
    """

    def get(self, request):
        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data)


class CidadeAPIView(APIView):
    """
        API Cidade
    """

    def get(self, request):
        cidades = Cidade.objects.all()
        serializer = CidadeSerializer(cidades, many=True)
        return Response(serializer.data)


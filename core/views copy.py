from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


    def post(self, request):
        serializer = EstadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class CidadeAPIView(APIView):
    """
        API Cidade
    """

    def get(self, request):
        cidades = Cidade.objects.all()
        serializer = CidadeSerializer(cidades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CidadeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
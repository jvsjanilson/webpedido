from rest_framework import serializers

from core.models import Estado, Cidade


class EstadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estado
        fields = (
            'id',
            'uf',
            'nome'
        )


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = (
            'nome',
            'estado'
        )


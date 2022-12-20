from django.db import models

class Estado(models.Model):
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.uf


class Cidade(models.Model):
    nome = models.CharField(max_length=60)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome


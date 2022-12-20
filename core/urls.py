from django.urls import path

from core.views import EstadoAPIView, CidadeAPIView

urlpatterns = [
    path('estados/', EstadoAPIView.as_view(), name='estados'),
    path('cidades/', CidadeAPIView.as_view(), name='cidades'),
]

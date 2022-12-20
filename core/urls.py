from django.urls import path

from core.views import EstadosAPIView, CidadesAPIView, EstadoAPIView, CidadeAPIView

urlpatterns = [
    path('estados/', EstadosAPIView.as_view(), name='estados'),
    path('estados/<int:pk>', EstadoAPIView.as_view(), name='estado'),
    path('estados/<int:estado_pk>/cidades', CidadesAPIView.as_view(), name='estado_cidades'),
    path('cidades/', CidadesAPIView.as_view(), name='cidades'),
    path('cidades/<int:pk>', CidadeAPIView.as_view(), name='cidade'),
]

from django.urls import path
from .views import (
    buscar_cliente, index,
    exportar_clientes_excel,
    exportar_fidelizados_excel,
    exportar_cliente_por_documento
)

urlpatterns = [
    path('', index),
    path('cliente', buscar_cliente),
    path('exportar/clientes', exportar_clientes_excel),
    path('exportar/fidelizados', exportar_fidelizados_excel),
    path('exportar/cliente', exportar_cliente_por_documento),
]
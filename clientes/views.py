from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Compra
from .serializers import ClienteSerializer
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.db.models import Sum

@api_view(['GET'])
def buscar_cliente(request):
    tipo_documento = request.GET.get('tipo_documento')
    numero_documento = request.GET.get('numero_documento')

    if not tipo_documento or not numero_documento:
        return JsonResponse({'error': 'Debe proporcionar tipo y número de documento'}, status=400)

    cliente = Cliente.objects.filter(
        tipo_documento__nombre=tipo_documento,
        numero_documento=numero_documento
    ).first()

    if cliente:
        return Response(ClienteSerializer(cliente).data)
    return Response({'error': 'Cliente no encontrado'}, status=404)




def index(request):
    return render(request, 'index.html')

def exportar_clientes_excel(request):
    clientes = Cliente.objects.all()
    data = [{
        'Tipo Documento': c.tipo_documento.nombre,
        'Número Documento': c.numero_documento,
        'Nombre': c.nombre,
        'Apellido': c.apellido,
        'Correo': c.correo,
        'Teléfono': c.telefono,
    } for c in clientes]

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="clientes.xlsx"'
    df.to_excel(response, index=False)
    return response

def exportar_fidelizados_excel(request):
    hace_30_dias = datetime.today() - timedelta(days=30)

    datos = []

    for cliente in Cliente.objects.all():
        total = Compra.objects.filter(cliente=cliente, fecha__gte=hace_30_dias).aggregate(Sum('monto'))['monto__sum'] or 0
        if total >= 5000000:
            datos.append({
                'Documento': cliente.numero_documento,
                'Nombre': cliente.nombre,
                'Apellido': cliente.apellido,
                'Correo': cliente.correo,
                'Teléfono': cliente.telefono,
                'Total Compras Último Mes': total,
            })

    df = pd.DataFrame(datos)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="clientes_fidelizados.xlsx"'
    df.to_excel(response, index=False)
    return response

def exportar_cliente_por_documento(request):
    tipo = request.GET.get('tipo_documento')
    numero = request.GET.get('numero_documento')

    if not tipo or not numero:
        return HttpResponse("Tipo y número de documento requeridos", status=400)

    cliente = Cliente.objects.filter(
        tipo_documento__nombre=tipo,
        numero_documento=numero
    ).first()

    if not cliente:
        return HttpResponse("Cliente no encontrado", status=404)

    compras = Compra.objects.filter(cliente=cliente)
    total_compras = compras.aggregate(Sum('monto'))['monto__sum'] or 0

    data = [{
        'Tipo Documento': cliente.tipo_documento.nombre,
        'Número Documento': cliente.numero_documento,
        'Nombre': cliente.nombre,
        'Apellido': cliente.apellido,
        'Correo': cliente.correo,
        'Teléfono': cliente.telefono,
        'Total Compras': total_compras
    }]

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{cliente.numero_documento}.xlsx"'
    df.to_excel(response, index=False)
    return response



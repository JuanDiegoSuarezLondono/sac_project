import os
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sac_project.settings')
django.setup()

from clientes.models import Cliente, TipoDocumento, Compra

# Limpieza previa
Compra.objects.all().delete()
Cliente.objects.all().delete()
TipoDocumento.objects.all().delete()

# Crear tipos de documento
tipos = ['NIT', 'Cédula', 'Pasaporte']
tipo_objs = {nombre: TipoDocumento.objects.create(nombre=nombre) for nombre in tipos}

# Crear clientes
for i in range(10):
    tipo = random.choice(list(tipo_objs.values()))
    cliente = Cliente.objects.create(
        tipo_documento=tipo,
        numero_documento=f"{i+1000000000}",
        nombre=f"Nombre{i}",
        apellido=f"Apellido{i}",
        correo=f"cliente{i}@correo.com",
        telefono=f"300123450{i}"
    )
    
    # Crear compras
    for j in range(3):#random.randint(1, 5)):
        fecha = date.today() - timedelta(days=random.randint(0, 60))  # últimas 2 meses
        monto = random.choice([100000, 500000, 2000000, 4000000, 1000000])
        Compra.objects.create(
            cliente=cliente,
            fecha=fecha,
            monto=monto,
            descripcion=f"Compra {j+1} de {cliente.nombre}"
        )

# Cliente fiel con más de 5 millones en el último mes
vip = Cliente.objects.create(
    tipo_documento=tipo_objs["Cédula"],
    numero_documento="1049636949",
    nombre="Cliente VIP Ultra Delux Super Chingon 4K",
    apellido="Juanito Londoño",
    correo="suarezlondonjuandiego@protonmail.com",
    telefono="3212357470"
    )
for i in range(3):
    Compra.objects.create(
        cliente=vip,
        fecha=date.today() - timedelta(days=i*2),
        monto=2000000,
        descripcion=f"Compra grande {i+1}"
    )

print("Datos cargados correctamente.")

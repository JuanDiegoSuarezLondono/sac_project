# Documentacion Tecnica SAC
## Estructura del proyecto
sac\_project/

|-- clientes/              # Modulo de consulta de clientes

|   |-- models.py          # Modelos de Cliente, Compra y TipoDocumento

|   |-- views.py           # API

|   |-- urls.py            # Rutas de la app

|  |-- templates/             # HTML con el formulario

│        |-- index.html

|--  poblar.py              # Script para insertar datos de prueba en la base de datos

|-- manage.py

|-- sac\_project/           # Configuración principal del proyecto

|   |--  settings.py

## Endpoints disponibles

|**Ruta**|**Método**|**Descripción**|
| :-: | :-: | :-: |
|/|GET|Pagina default con redireccionamiento al formulario de búsqueda|
|/api|GET|Pagina con formulario de búsqueda|
|/api/cliente|GET|Consulta un cliente|
|/api/exportar/cliente|GET|Exporta un solo cliente (Excel)|
|/api/exportar/clientes|GET|Exporta todos los clientes (Excel)|
|/api/exportar/fidelizados|GET|Exporta un solo los clientes fidelizados (Excel)|

## Modelos Clave
### Cliente
- tipo-documento (FK)
- numero\_documento
- nombre
- apellido
- correo
- teléfono
### TipoDocumento
- nombre
### Compra
- cliente (FK)
- fecha
- monto
- descripcion
## Datos de Prueba
Los datos de prueba son creados con poblar.py e incluyen:

- 10 clientes normales y uno VIP con mas de $5M en compras del último mes/recientes.
- Compras aleatorias en las ultimas semanas para los clientes no VIP

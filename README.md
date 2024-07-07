# Sistema para registro de infracciones de tránsito
## Desafío técnico
1. Clonar el repositorio
2. Ubicarse en la raiz del proyecto.

### Sin Docker:
1. Crear un entorno virtual `python -m virtualenv .venv`
4. Activar el entorno virtual `source ./.venv/bin/activate`
5. Instalar las dependencias `pip install -r requirements.txt`
6. Crear las migraciones `python manage.py makemigrations`
7. Ejecutar las migraciones `python manage.py migrate`

#### Con Docker:
Como pre-requisito se debe tener instalado docker en la máquina donde se probará. https://docs.docker.com/engine/install/ 

En una terminal:
1. Ejecutar el comando: `docker build -t nombre_de_la_imagen .` 
4. Ejecutar `docker run -d -p 8000:8000 --name nombre_para_contenedor nombre_de_la_imagen`. Debemos asegurarnos de que los puertos están bien mapeados y darle un nombre adecuado al contenedor.
5. Si todo es exitoso para ingresar a la consola del contenedor `docker exec -it nombre_para_contenedor /bin/bash`
Aquí se podrán ejecutar todos los comandos que necesite el proyecto.
    - `python manage.py makemigrations`
    - `python manage.py migrate` 
5. Para detener el contenedor `docker stop nombre_para_contenedor`
6. Para ejecutar el contenedor nuevamente `docker start nombre_para_contenedor`
### Uso de la API:
Los llamados se pueden hacer desde la consola y/o con herramientas como Postman

Generar el Token de Acceso (POST):
```
Body:
{
    "identification": <numero_unico_identificatorio(nui)>
}
-----------------
curl -X POST http://tu_dominio.com/api/token/ \ -H "Content-Type: application/json" \ -d '{"identification": <numero_unico_identificatorio(nui)>}'

Respuesta:
{
    "status": "success",
    "data": {
        "officer": "officer_name",
        "refresh": "<refresh_token>",
        "access": "<access_token>"
    }
}
```

Refrescar el Token de Acceso (POST):
```
Body:
{
    "refresh": "<refresh_token>"
}
-----------------
curl -X POST http://127.0.0.1:8000/register_app/api/token/ \ -H "Content-Type: application/json" \ -d '{"refresh": "<refresh_token>"'

Respuesta:
{
    "status": "success",
    "data": {
        "officer": "officer_name",
        "refresh": "<refresh_token>",
        "access": "<access_token>"
    }
}
```

Registrar una nueva infracción (POST):
```
curl -X POST http://127.0.0.1:8000/register_app/api/create-infraction/ \ -H "Authorization: Bearer <access_token>" \ -H "Content-Type: application/json" \ -d '{"patente": "<patente>", "timestamp": "<fecha y hora>", "comment": "<comentario>"}'


Respuesta:
{
    "status": 200,
    "object": {
        "vehicle": "patente - persona",
        "timestamp": "fecha y hora,
        "comment": "Comentario"
    },
    "msj": "Infracción registrada con éxito."
}
```

Generar informe (GET):
```
En la URL:
http://127.0.0.1:8000/register_app/api/generar-informe?email=<correo_persona>

Respuesta:
{
   "status": 200,
    "objects": [
        {
            "vehicle": "patente - persona",
            "timestamp": "fecha y hora",
            "comment": "Commentario"
        },
        {
            "vehicle": "patente - persona",
            "timestamp": "fecha y hora",
            "comment": "Commentario"
        }
    ],
    "msj": "Infracciones encontradas."
}
```

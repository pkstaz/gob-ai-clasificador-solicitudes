
# Clasificador de Solicitudes Ciudadanas - API de Inferencia

> **Nota:** Este proyecto es ficticio, creado únicamente para fines de demostración y no representa datos reales ni solicitudes ciudadanas auténticas.

Este proyecto despliega un modelo de clasificación de solicitudes ciudadanas como una API REST en un contenedor, descargando el modelo desde un almacenamiento S3/MinIO.

## Estructura
- `src/app.py`: Código de la API FastAPI.
- `requirements.txt`: Dependencias del proyecto.
- `Dockerfile`: Imagen para contenerizar la API.
- El modelo `.pkl` se almacena en S3/MinIO y se descarga al iniciar el contenedor.

## Dependencias principales
- fastapi
- pydantic
- boto3
- joblib
- pandas
- scikit-learn
- wordcloud (requiere gcc y python3-dev)

## Variables de entorno necesarias
- `AWS_ACCESS_KEY_ID`: Usuario S3/MinIO
- `AWS_SECRET_ACCESS_KEY`: Clave S3/MinIO
- `AWS_S3_ENDPOINT`: URL del endpoint S3/MinIO
- `AWS_S3_BUCKET`: Nombre del bucket
- `S3_OBJECT_NAME`: Nombre del archivo modelo `.pkl`

## Construcción y ejecución

### 1. Construir la imagen
```sh
podman build -t clasificador-api ./entrenamiento-modelo
```

### 2. Ejecutar el contenedor
```sh
podman run -p 8080:8080 \
  -e AWS_ACCESS_KEY_ID=minio \
  -e AWS_SECRET_ACCESS_KEY=minio123 \
  -e AWS_S3_ENDPOINT=https://minio-api-prov-bs-as.apps.cluster-l2lrz.l2lrz.sandbox2518.opentlc.com \
  -e AWS_S3_BUCKET=tu_bucket \
  -e S3_OBJECT_NAME=clasificador_solicitudes_pba_v1.pkl \
  clasificador-api
```

## Consumo de la API

### Endpoint `/predict`
- Método: POST
- Entrada:
```json
{
  "texto": "Ejemplo de solicitud ciudadana para clasificar"
}
```
- Respuesta:
```json
{
  "prediccion": "Ministerio de Seguridad",
  "confianza": 0.92
}
```

### Ejemplo con curl
```sh
curl -X POST "http://localhost:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{"texto": "Ejemplo de solicitud ciudadana para clasificar"}'
```

## Notas
- El modelo se descarga automáticamente desde S3/MinIO al iniciar el contenedor.
- Si el modelo soporta `predict_proba`, se devuelve la confianza en la predicción.
- Revisa los logs del contenedor para depuración de errores de conexión o descarga.

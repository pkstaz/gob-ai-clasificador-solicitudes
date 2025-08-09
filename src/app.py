from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import boto3

app = FastAPI()

# Leer credenciales S3 desde variables de entorno
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
endpoint_url = os.getenv('AWS_S3_ENDPOINT')
bucket_name = os.getenv('AWS_S3_BUCKET')
object_name = os.getenv("S3_OBJECT_NAME", "clasificador_solicitudes_pba_v1.pkl")
local_model_path = "/tmp/model.pkl"

# Descargar el modelo desde S3 si no existe localmente
import logging

if not os.path.exists(local_model_path):
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        endpoint_url=endpoint_url
    )
    try:
        logging.info(f"Descargando modelo desde S3: bucket={bucket_name}, objeto={object_name}")
        s3.download_file(bucket_name, object_name, local_model_path)
        logging.info("Modelo descargado correctamente.")
    except Exception as e:
        logging.error(f"Error al descargar el modelo desde S3: {e}")
        raise RuntimeError(f"No se pudo descargar el modelo desde S3: {e}")


# Cargar el modelo, soportando ambos formatos
try:
    model_bundle = joblib.load(local_model_path)
    if isinstance(model_bundle, dict) and 'model' in model_bundle:
        model = model_bundle['model']
        vectorizer = model_bundle.get('vectorizer', None)
    else:
        model = model_bundle
        vectorizer = None
except Exception as e:
    import sys
    print(f"Error al cargar el modelo: {e}", file=sys.stderr)
    raise RuntimeError(f"No se pudo cargar el modelo: {e}")

class InputData(BaseModel):
    texto: str

@app.post("/predict")
async def predict(data: InputData):
    # Si existe vectorizer, transformar el texto
    if 'vectorizer' in locals() and vectorizer is not None:
        X = vectorizer.transform([data.texto])
    else:
        X = pd.Series([data.texto])
    pred = model.predict(X)
    # Calcular confianza si el modelo tiene predict_proba
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)
        indice = list(model.classes_).index(pred[0])
        confianza = float(proba[0][indice])
    else:
        confianza = None
    return {
        "prediccion": pred[0],
        "confianza": confianza
    }

@app.get("/")
def root():
    return {"message": "API de inferencia del clasificador de solicitudes"}

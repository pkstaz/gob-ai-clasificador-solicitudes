import kfp
from kfp import dsl

@dsl.component(base_image="registry.access.redhat.com/ubi9/python-3.11")
def generar_datos():
    import os
    from generar_dataset import GeneradorSolicitudesCiudadanas
    import pandas as pd
    os.makedirs('data', exist_ok=True)
    generador = GeneradorSolicitudesCiudadanas()
    df = generador.generar_dataset(5000)
    df.to_csv('data/solicitudes_ciudadanas_pba.csv', index=False)
    print("✅ Dataset generado y guardado")

@dsl.component(base_image="registry.access.redhat.com/ubi9/python-3.11")
def entrenar_modelo():
    import pandas as pd
    import joblib
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    df = pd.read_csv('data/solicitudes_ciudadanas_pba.csv')
    X = df['texto_solicitud']
    y = df['departamento_destino']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    modelo_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2), lowercase=True)),
        ('clasificador', LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced'))
    ])
    modelo_pipeline.fit(X_train, y_train)
    os.makedirs('models', exist_ok=True)
    joblib.dump(modelo_pipeline, 'models/clasificador_solicitudes_pba_v1.pkl')
    print("✅ Modelo entrenado y guardado")

@dsl.component(base_image="registry.access.redhat.com/ubi9/python-3.11")
def evaluar_modelo():
    import pandas as pd
    import joblib
    from sklearn.metrics import accuracy_score, precision_recall_fscore_support
    df = pd.read_csv('data/solicitudes_ciudadanas_pba.csv')
    X = df['texto_solicitud']
    y = df['departamento_destino']
    modelo_pipeline = joblib.load('models/clasificador_solicitudes_pba_v1.pkl')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    y_pred = modelo_pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    print(f"Precisión: {accuracy:.3f}, Precision: {precision:.3f}, Recall: {recall:.3f}, F1: {f1:.3f}")

@dsl.component(base_image="registry.access.redhat.com/ubi9/python-3.11")
def subir_modelo_s3():
    import os
    import boto3
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    endpoint_url = os.getenv('S3_ENDPOINT_URL')
    bucket_name = os.getenv('S3_BUCKET_NAME')
    object_name = "modelos/clasificador_solicitudes_pba_v1.pkl"
    local_path = "models/clasificador_solicitudes_pba_v1.pkl"
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        endpoint_url=endpoint_url
    )
    s3.upload_file(local_path, bucket_name, object_name)
    print(f"✅ Modelo guardado en S3: s3://{bucket_name}/{object_name}")

@dsl.pipeline(name="Pipeline Clasificador Solicitudes")
def clasificador_pipeline():
    generar_datos()
    entrenar_modelo()
    evaluar_modelo()
    subir_modelo_s3()

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(clasificador_pipeline, "pipeline_clasificador.yaml")

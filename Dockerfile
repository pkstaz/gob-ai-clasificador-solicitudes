# Dockerfile para API de inferencia con FastAPI y modelo S3
FROM python:3.11-slim

WORKDIR /app

# Instala gcc y dependencias para wordcloud
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY src/app.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

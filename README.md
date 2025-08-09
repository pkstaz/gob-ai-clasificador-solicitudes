### Ejemplos adicionales

```sh
# Ejemplo 1: Reclamo de seguridad
curl -X POST "http://localhost:8080/predict" \
	-H "Content-Type: application/json" \
	-d '{"texto": "Hay robos frecuentes en mi barrio, solicito patrullaje policial."}'

# Ejemplo 2: Solicitud de salud
curl -X POST "http://localhost:8080/predict" \
	-H "Content-Type: application/json" \
	-d '{"texto": "Necesito turno para vacunación contra la gripe en el hospital municipal."}'

# Ejemplo 3: Consulta sobre educación
curl -X POST "http://localhost:8080/predict" \
	-H "Content-Type: application/json" \
	-d '{"texto": "¿Cuándo comienzan las inscripciones para las escuelas públicas?"}'
```

Cada ejemplo devolverá el departamento predicho y el nivel de confianza según el modelo entrenado.
# 🏛️ Demo OpenShift AI: Clasificación Inteligente de Solicitudes Ciudadanas
> **Nota:** Este proyecto es ficticio, creado únicamente para fines de demostración y no representa datos reales ni solicitudes ciudadanas auténticas.
## Provincia de Buenos Aires - Transformación Digital del Sector Público

![OpenShift AI](https://img.shields.io/badge/OpenShift-AI-red?style=for-the-badge&logo=redhat)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-lightblue?style=for-the-badge&logo=mlflow)

---

## 📋 Descripción del Proyecto

Este proyecto es una **demostración práctica de MLOps** usando OpenShift AI para resolver un problema real del sector público: la clasificación automática de solicitudes ciudadanas en la Provincia de Buenos Aires.

### 🎯 Caso de Uso

**Problema:** Miles de solicitudes ciudadanas (quejas, consultas, sugerencias, trámites) llegan diariamente y deben ser clasificadas manualmente para derivarlas al departamento correcto.

**Solución:** Sistema de clasificación automática usando Machine Learning que:
- ✅ Reduce tiempo de procesamiento de días a minutos
- ✅ Mejora precisión en la derivación (85%+ accuracy)
- ✅ Libera recursos humanos para tareas de mayor valor
- ✅ Proporciona métricas para mejorar la gestión pública

### 🏛️ Departamentos Cubiertos

- Ministerio de Salud
- Ministerio de Educación
- Ministerio de Seguridad
- Ministerio de Obras Públicas
- Ministerio de Desarrollo Social
- Ministerio de Producción
- Ministerio de Ambiente
- ARBA (Recaudación)
- Registro de Personas

---

## 🚀 Inicio Rápido

## Consumo de la API de Inferencia

El modelo se expone como una API REST (FastAPI) en el endpoint `/predict`.

### Ejemplo de uso con curl

```sh
curl -X POST "http://localhost:8080/predict" \
	-H "Content-Type: application/json" \
	-d '{"texto": "Ejemplo de solicitud ciudadana para clasificar"}'
```

### Respuesta esperada

```json
{
	"prediccion": "Ministerio de Salud",
	"confianza": 0.24
}
```

Puedes cambiar el texto para probar diferentes solicitudes. Si el modelo está desplegado en otro endpoint, reemplaza la URL por la correspondiente.

### Prerrequisitos

- Python 3.8+
- Jupyter Notebook
- VS Code (recomendado)

### Instalación

1. **Clonar el repositorio** (o usar este workspace)
```bash
cd gob-ai-clasificador-solicitudes/model
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la demo**
```bash
jupyter notebook notebooks/demo_openshift_ai_clasificacion_solicitudes.ipynb
```

### Demo en 15 minutos

La demostración está estructurada para una presentación de **15 minutos**:

1. **Contexto (2 min)**: Problema y solución propuesta
2. **Datos (2 min)**: Exploración del dataset de 5000 solicitudes
3. **Entrenamiento (3 min)**: Pipeline de ML con TF-IDF + Logistic Regression
4. **Evaluación (3 min)**: Métricas de precisión y matriz de confusión
5. **Producción (3 min)**: Simulación de clasificación en tiempo real
6. **Monitoreo (2 min)**: Dashboard de MLOps y alertas automáticas

---

## 📊 Resultados Esperados

### Métricas Técnicas
- **Precisión**: 85%+ en clasificación automática
- **Tiempo de respuesta**: <100ms por solicitud
- **Capacidad**: 200+ solicitudes/día escalable
- **Cobertura**: 9 departamentos provinciales

### Impacto en la Gestión
- **Reducción de tiempo**: 70% en procesamiento inicial
- **Ahorro**: ~49 horas diarias de trabajo manual
- **ROI**: Demostrable y medible
- **Satisfacción ciudadana**: Respuestas más rápidas

---

## 📁 Estructura del Proyecto

```
gob-ai-clasificador-solicitudes/model/
├── notebooks/
│   └── demo_openshift_ai_clasificacion_solicitudes.ipynb  # Demo principal
├── src/
│   └── generar_dataset.py                                # Generador de datos sintéticos
├── data/
│   └── solicitudes_ciudadanas_pba.csv                   # Dataset generado
├── models/
│   ├── clasificador_solicitudes_pba_v1.pkl              # Modelo entrenado
│   └── stats_modelo_v1.json                             # Métricas del modelo
├── requirements.txt                                      # Dependencias Python
└── README.md                                            # Este archivo
```

---

## 🔧 Tecnologías Utilizadas

### MLOps Stack
- **OpenShift AI**: Plataforma de MLOps empresarial
- **MLflow**: Tracking de experimentos y registro de modelos
- **Jupyter**: Entorno de desarrollo interactivo

### Machine Learning
- **Scikit-learn**: Algoritmos de clasificación
- **TF-IDF**: Vectorización de texto
- **Logistic Regression**: Modelo base (interpretable y eficiente)

### Visualización
- **Plotly**: Gráficos interactivos para dashboards
- **Matplotlib/Seaborn**: Análisis exploratorio
- **Pandas**: Manipulación de datos

---

## 👥 Audiencia Objetivo

Esta demo está diseñada para una **audiencia mixta**:

### 🏛️ Funcionarios Públicos y Tomadores de Decisión
- Enfoque en valor de negocio y ROI
- Métricas de impacto en la gestión pública
- Roadmap de implementación clara

### 👨‍💻 Equipos Técnicos
- Detalles de implementación MLOps
- Arquitectura del sistema
- Consideraciones de producción

### 📈 Analistas y Gestores de Proyectos
- Métricas de rendimiento
- Planes de despliegue
- Gestión del cambio

---

## 🔄 Flujo de MLOps Demostrado

1. **📊 Ingesta de Datos**: Dataset sintético realista
2. **🔧 Preprocesamiento**: TF-IDF vectorization
3. **🤖 Entrenamiento**: Pipeline automatizado con validación
4. **📈 Evaluación**: Métricas detalladas por departamento
5. **🚀 Despliegue**: Simulación de inferencia en tiempo real
6. **📊 Monitoreo**: Dashboard con alertas automáticas
7. **🔄 Mejora Continua**: Detección de drift y reentrenamiento

---

## 📈 Métricas Clave para Gestión

### Operativas
- **Solicitudes procesadas/día**: 200+ (escalable)
- **Tiempo de respuesta promedio**: <100ms
- **Disponibilidad del servicio**: 99.9%
- **Precisión de clasificación**: 85%+

### De Negocio
- **Ahorro de tiempo**: 70% reducción en procesamiento
- **Costo por solicitud**: Reducción significativa
- **Satisfacción ciudadana**: Mejora en tiempos de respuesta
- **Eficiencia del personal**: Enfoque en tareas de mayor valor

---

## 🔮 Próximos Pasos

### Fase 1: Piloto (3 meses)
- [ ] Implementar en 2-3 departamentos de alto volumen
- [ ] Validar con datos reales
- [ ] Ajustar modelo según feedback

### Fase 2: Expansión (6 meses)
- [ ] Rollout completo a 9 departamentos
- [ ] Integración con sistemas existentes
- [ ] Capacitación del personal

### Fase 3: Optimización (12 meses)
- [ ] Clasificación completamente automática
- [ ] Analytics avanzados
- [ ] Expansión a otros casos de uso

---

## 🤝 Contacto y Soporte

Para preguntas sobre esta demostración o implementación en su organización:

- **Equipo de Transformación Digital**
- **OpenShift AI Specialists**
- **MLOps Consultants**

---

## 📄 Licencia

Este proyecto es una demostración educativa para el sector público argentino.

---

**🇦🇷 Gobierno de la Provincia de Buenos Aires**  
**Transformación Digital del Sector Público**

*"De la promesa al impacto real con OpenShift AI"*

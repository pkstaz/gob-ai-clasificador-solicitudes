"""
Generador de dataset sintético para solicitudes ciudadanas
Provincia de Buenos Aires - Demo OpenShift AI
"""

import pandas as pd
import random
from faker import Faker
import json
from datetime import datetime, timedelta

# Configurar Faker para español argentino
fake = Faker('es_AR')

class GeneradorSolicitudesCiudadanas:
    def __init__(self):
        self.departamentos = [
            "Ministerio de Salud",
            "Ministerio de Educación", 
            "Ministerio de Seguridad",
            "Ministerio de Obras Públicas",
            "Ministerio de Desarrollo Social",
            "Ministerio de Producción",
            "Ministerio de Ambiente",
            "ARBA",
            "Registro de Personas"
        ]
        
        self.tipos_solicitud = ["Queja", "Consulta", "Sugerencia", "Trámite"]
        
        # Templates realistas por departamento y tipo
        self.templates = {
            "Ministerio de Salud": {
                "Queja": [
                    "Demora excesiva en la atención en el hospital {hospital}. Esperé {horas} horas para ser atendido.",
                    "Falta de medicamentos en el centro de salud de {localidad}. No tienen {medicamento}.",
                    "Personal médico maltrata a los pacientes en {hospital}. Necesitan capacitación urgente.",
                    "No hay ambulancias disponibles en {localidad}. Es una emergencia sanitaria."
                ],
                "Consulta": [
                    "¿Cómo puedo inscribirme al programa de vacunación contra {enfermedad}?",
                    "¿Qué documentación necesito para acceder a medicación gratuita?",
                    "¿Cuáles son los horarios de atención del centro de salud de {localidad}?",
                    "¿Cómo solicito una ambulancia para traslado programado?"
                ],
                "Sugerencia": [
                    "Propongo ampliar los horarios de atención en el hospital {hospital}.",
                    "Sería útil implementar turnos online para el centro de salud de {localidad}.",
                    "Sugiero más campañas de prevención en {tema_salud}.",
                    "Deberían instalar más consultorios móviles en zonas rurales."
                ],
                "Trámite": [
                    "Solicito certificado de discapacidad para mi {familiar}.",
                    "Necesito renovar mi credencial de obra social provincial.",
                    "Quiero inscribirme en el programa de medicación gratuita.",
                    "Solicito autorización para traslado médico interprovincial."
                ]
            },
            "Ministerio de Educación": {
                "Queja": [
                    "La escuela {escuela} de {localidad} no tiene calefacción funcionando.",
                    "Faltan docentes en la escuela {escuela}. Los chicos pierden clases constantemente.",
                    "El transporte escolar no pasa por mi barrio en {localidad}.",
                    "La infraestructura de la escuela {escuela} está deteriorada y es peligrosa."
                ],
                "Consulta": [
                    "¿Cómo inscribo a mi hijo en el jardín de infantes de {localidad}?",
                    "¿Qué documentación necesito para el pase de escuela?",
                    "¿Cuándo abren las inscripciones para secundaria técnica?",
                    "¿Cómo solicito una beca estudiantil provincial?"
                ],
                "Sugerencia": [
                    "Propongo implementar educación sexual integral en todas las escuelas.",
                    "Sería bueno tener más talleres de oficios en las escuelas técnicas.",
                    "Sugiero crear un programa de tutorías para estudiantes con dificultades.",
                    "Deberían instalar wifi gratuito en todas las escuelas públicas."
                ],
                "Trámite": [
                    "Solicito certificado analítico de estudios secundarios.",
                    "Necesito legalizar mi título universitario.",
                    "Quiero inscribirme en los cursos de capacitación docente.",
                    "Solicito constancia de alumno regular para mi hijo."
                ]
            },
            "Ministerio de Seguridad": {
                "Queja": [
                    "Hay robos constantes en el barrio {barrio} de {localidad} y no viene la policía.",
                    "Los patrulleros no funcionan en la comisaría de {localidad}.",
                    "Denuncié violencia doméstica hace una semana y no hay respuesta.",
                    "La comisaría {numero} no atiende las 24 horas como debería."
                ],
                "Consulta": [
                    "¿Cómo puedo denunciar un robo online?",
                    "¿Qué documentos necesito para tramitar el DNI?",
                    "¿Cuáles son los requisitos para ingresar a la policía provincial?",
                    "¿Dónde puedo consultar el estado de mi denuncia?"
                ],
                "Sugerencia": [
                    "Propongo más patrullajes nocturnos en {localidad}.",
                    "Sería útil instalar cámaras de seguridad en {lugar}.",
                    "Sugiero crear una app para denuncias ciudadanas.",
                    "Deberían implementar botones antipánico en lugares públicos."
                ],
                "Trámite": [
                    "Solicito certificado de antecedentes penales.",
                    "Necesito renovar mi DNI que está vencido.",
                    "Quiero registrar mi arma de fuego legalmente.",
                    "Solicito constancia de domicilio para trámites bancarios."
                ]
            },
            "Ministerio de Obras Públicas": {
                "Queja": [
                    "La ruta {numero} está en pésimo estado entre {ciudad1} y {ciudad2}.",
                    "No hay alumbrado público en {barrio} de {localidad}.",
                    "Las cloacas están colapsadas en mi cuadra hace {dias} días.",
                    "El puente de {localidad} está cerrado y no hay alternativa."
                ],
                "Consulta": [
                    "¿Cuándo van a repavimentar la calle {calle} de {localidad}?",
                    "¿Cómo solicito conexión de agua potable para mi barrio?",
                    "¿Qué empresa se encarga del mantenimiento de semáforos?",
                    "¿Cuál es el cronograma de obras para la ruta {numero}?"
                ],
                "Sugerencia": [
                    "Propongo instalar reductores de velocidad en {lugar}.",
                    "Sería útil crear más ciclovías en {localidad}.",
                    "Sugiero mejorar el drenaje pluvial en {barrio}.",
                    "Deberían construir más paradas de colectivo techadas."
                ],
                "Trámite": [
                    "Solicito permiso para obra en vía pública.",
                    "Necesito autorización para conexión de agua en mi propiedad.",
                    "Quiero denunciar una pérdida de agua en la vía pública.",
                    "Solicito reparación del pavimento frente a mi casa."
                ]
            }
            # Continúo con más departamentos...
        }
        
        # Completar templates para otros departamentos
        self._completar_templates()
    
    def _completar_templates(self):
        """Completa los templates para el resto de departamentos"""
        
        self.templates["Ministerio de Desarrollo Social"] = {
            "Queja": [
                "No recibí la ayuda social prometida hace {meses} meses.",
                "El centro comunitario de {localidad} está cerrado sin aviso.",
                "Los trabajadores sociales no visitan {barrio} desde hace tiempo.",
                "La tarjeta alimentaria no funciona en los comercios de {localidad}."
            ],
            "Consulta": [
                "¿Cómo me inscribo en el programa de asistencia alimentaria?",
                "¿Qué requisitos necesito para acceder a la vivienda social?",
                "¿Dónde puedo inscribirme en los cursos de capacitación laboral?",
                "¿Cómo solicito ayuda para adultos mayores?"
            ],
            "Sugerencia": [
                "Propongo más centros de día para adultos mayores.",
                "Sería útil crear más cooperativas de trabajo en {localidad}.",
                "Sugiero ampliar los programas de asistencia a jóvenes.",
                "Deberían instalar más merenderos comunitarios."
            ],
            "Trámite": [
                "Solicito inscripción en el programa Potenciar Trabajo.",
                "Necesito renovar mi tarjeta alimentaria.",
                "Quiero inscribirme en el programa de microcréditos.",
                "Solicito asistencia económica por situación de vulnerabilidad."
            ]
        }
        
        self.templates["Ministerio de Producción"] = {
            "Queja": [
                "No aprueban mi proyecto productivo hace {meses} meses sin explicación.",
                "La oficina de habilitaciones comerciales de {localidad} nunca está abierta.",
                "Cobran tasas municipales excesivas para pequeños comercios.",
                "No hay apoyo real para emprendedores en {localidad}."
            ],
            "Consulta": [
                "¿Cómo accedo a créditos para pymes?",
                "¿Qué requisitos necesito para habilitar un comercio?",
                "¿Dónde puedo capacitarme en gestión empresarial?",
                "¿Cómo me inscribo como monotributista social?"
            ],
            "Sugerencia": [
                "Propongo crear un polo industrial en {localidad}.",
                "Sería útil simplificar los trámites para emprendedores.",
                "Sugiero más ferias de productos locales.",
                "Deberían crear incubadoras de empresas tecnológicas."
            ],
            "Trámite": [
                "Solicito habilitación comercial para mi negocio.",
                "Necesito certificado de productor agropecuario.",
                "Quiero inscribirme en el registro de proveedores del estado.",
                "Solicito subsidio para compra de maquinaria agrícola."
            ]
        }
        
        self.templates["Ministerio de Ambiente"] = {
            "Queja": [
                "Hay contaminación del agua en el arroyo {nombre} de {localidad}.",
                "Empresa {empresa} contamina el aire sin control en {localidad}.",
                "Talan árboles indiscriminadamente en {lugar}.",
                "Hay un basural clandestino en {barrio} que nadie controla."
            ],
            "Consulta": [
                "¿Cómo denuncio un delito ambiental?",
                "¿Qué días pasa la recolección de residuos reciclables?",
                "¿Cómo solicito la poda de árboles públicos?",
                "¿Dónde puedo consultar la calidad del aire en mi zona?"
            ],
            "Sugerencia": [
                "Propongo más campañas de reciclaje en las escuelas.",
                "Sería útil crear más espacios verdes en {localidad}.",
                "Sugiero controles más estrictos a las industrias contaminantes.",
                "Deberían instalar más puntos de reciclaje en la ciudad."
            ],
            "Trámite": [
                "Solicito evaluación de impacto ambiental para mi proyecto.",
                "Necesito permiso para poda de árbol en mi propiedad.",
                "Quiero denunciar contaminación sonora de un comercio.",
                "Solicito inspección ambiental en empresa {empresa}."
            ]
        }
        
        self.templates["ARBA"] = {
            "Queja": [
                "Me llegó una factura de patente automotor incorrecta.",
                "No puedo pagar los impuestos online, el sistema no funciona.",
                "Las oficinas de ARBA de {localidad} siempre tienen largas colas.",
                "Me cobran impuesto inmobiliario por una propiedad que ya vendí."
            ],
            "Consulta": [
                "¿Cómo puedo adherirme al débito automático para impuestos?",
                "¿Dónde consulto el estado de cuenta de mis impuestos?",
                "¿Qué descuentos hay por pago anticipado?",
                "¿Cómo solicito una factura de libre deuda?"
            ],
            "Sugerencia": [
                "Propongo más oficinas de ARBA en el interior.",
                "Sería útil mejorar el sistema de turnos online.",
                "Sugiero descuentos mayores para pago anual anticipado.",
                "Deberían crear una app móvil para consultas rápidas."
            ],
            "Trámite": [
                "Solicito plan de pago para impuestos atrasados.",
                "Necesito certificado de libre deuda inmobiliaria.",
                "Quiero transferir la titularidad de un vehículo.",
                "Solicito exención de impuestos por discapacidad."
            ]
        }
        
        self.templates["Registro de Personas"] = {
            "Queja": [
                "Saqué turno para DNI hace {meses} meses y aún no me llamaron.",
                "El registro civil de {localidad} no atiende en los horarios publicados.",
                "Perdieron mi expediente de cambio de domicilio.",
                "No hay sistema para consultar el estado de mi trámite."
            ],
            "Consulta": [
                "¿Cómo saco turno para renovar mi DNI?",
                "¿Qué documentos necesito para inscribir a mi bebé?",
                "¿Dónde puedo cambiar el domicilio en mi DNI?",
                "¿Cómo obtengo partida de nacimiento legalizada?"
            ],
            "Sugerencia": [
                "Propongo más oficinas de registro en el interior.",
                "Sería útil poder hacer algunos trámites de forma remota.",
                "Sugiero turnos de tarde para personas que trabajan.",
                "Deberían modernizar el sistema de seguimiento de trámites."
            ],
            "Trámite": [
                "Solicito renovación de DNI por vencimiento.",
                "Necesito partida de defunción de mi {familiar}.",
                "Quiero inscribir el nacimiento de mi hijo.",
                "Solicito rectificación de datos en mi DNI."
            ]
        }
    
    def generar_solicitud(self, departamento, tipo):
        """Genera una solicitud realista para un departamento y tipo específico"""
        template = random.choice(self.templates[departamento][tipo])
        
        # Variables para reemplazar en templates
        variables = {
            'hospital': random.choice(['Hospital San Juan de Dios', 'Hospital Municipal', 'Hospital Evita', 'HIGA']),
            'localidad': fake.city(),
            'barrio': f"Barrio {fake.last_name()}",
            'horas': random.randint(2, 12),
            'medicamento': random.choice(['ibuprofeno', 'paracetamol', 'insulina', 'antihipertensivos']),
            'enfermedad': random.choice(['COVID-19', 'gripe', 'hepatitis B', 'sarampión']),
            'familiar': random.choice(['padre', 'madre', 'hijo', 'hija', 'esposo', 'esposa']),
            'escuela': f"Escuela N° {random.randint(1, 500)}",
            'numero': random.randint(1, 100),
            'dias': random.randint(1, 30),
            'meses': random.randint(1, 12),
            'calle': fake.street_name(),
            'ciudad1': fake.city(),
            'ciudad2': fake.city(),
            'lugar': random.choice(['plaza principal', 'centro comercial', 'estación de tren', 'hospital']),
            'tema_salud': random.choice(['diabetes', 'hipertensión', 'salud mental', 'adicciones']),
            'empresa': f"Empresa {fake.company()}",
            'nombre': fake.first_name()
        }
        
        # Reemplazar variables en el template
        solicitud = template
        for var, valor in variables.items():
            solicitud = solicitud.replace(f'{{{var}}}', str(valor))
        
        return solicitud
    
    def generar_dataset(self, n_solicitudes=500):
        """Genera un dataset completo de solicitudes"""
        datos = []
        
        for _ in range(n_solicitudes):
            departamento = random.choice(self.departamentos)
            tipo = random.choice(self.tipos_solicitud)
            
            solicitud = {
                'id': fake.uuid4(),
                'fecha': fake.date_between(start_date='-1y', end_date='today').isoformat(),
                'ciudadano_nombre': fake.name(),
                'ciudadano_dni': fake.random_int(min=10000000, max=99999999),
                'ciudadano_email': fake.email(),
                'ciudadano_telefono': fake.phone_number(),
                'localidad': fake.city(),
                'tipo_solicitud': tipo,
                'departamento_destino': departamento,
                'texto_solicitud': self.generar_solicitud(departamento, tipo),
                'prioridad': random.choice(['Baja', 'Media', 'Alta']),
                'estado': random.choice(['Pendiente', 'En proceso', 'Resuelta']),
                'canal_ingreso': random.choice(['Web', 'Presencial', 'Teléfono', 'Email'])
            }
            
            datos.append(solicitud)
        
        return pd.DataFrame(datos)

if __name__ == "__main__":
    import os
    
    generador = GeneradorSolicitudesCiudadanas()
    df = generador.generar_dataset(500)
    
    # Obtener el directorio del proyecto (un nivel arriba del src)
    proyecto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(proyecto_dir, 'data')
    
    # Crear directorio data si no existe
    os.makedirs(data_dir, exist_ok=True)
    
    # Guardar dataset
    csv_path = os.path.join(data_dir, 'solicitudes_ciudadanas_pba.csv')
    df.to_csv(csv_path, index=False)
    print(f"Dataset generado con {len(df)} solicitudes")
    print(f"Archivo guardado en: {csv_path}")
    print(f"Distribución por departamento:")
    print(df['departamento_destino'].value_counts())
    print(f"\nDistribución por tipo:")
    print(df['tipo_solicitud'].value_counts())

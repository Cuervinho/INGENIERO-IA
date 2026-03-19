# services/monitoring_service.py

"""
Servicio de monitoreo y alertas:    
- Obtiene datos clave para monitoreo (transacciones altas, alertas críticas, etc.)
- Evalúa reglas simples para detectar posibles riesgos
- Genera un resumen con insights y recomendaciones usando IA
"""

from services.query_executor import execute_query
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def get_monitoring_data(user):
    # 1. Transacciones altas
    transacciones_altas = execute_query("""
        SELECT COUNT(*)
        FROM transacciones t
        JOIN cuentas c ON t.id_cuenta = c.id_cuenta
        JOIN asociados a ON c.id_asociado = a.id_asociado
        WHERE t.monto > 10000000
        AND a.id_organizacion = ?
    """, (user.id_organizacion,))

    # 2. Alertas críticas
    alertas_criticas = execute_query("""
        SELECT COUNT(*)
        FROM alertas al
        JOIN asociados a ON al.id_asociado = a.id_asociado
        WHERE al.severidad = 'Critica'
        AND a.id_organizacion = ?
    """, (user.id_organizacion,))

    # 3. Total asociados
    asociados = execute_query("""
        SELECT COUNT(*)
        FROM asociados
        WHERE id_organizacion = ?
    """, (user.id_organizacion,))

    return {
        "transacciones_altas": transacciones_altas[0][0],
        "alertas_criticas": alertas_criticas[0][0],
        "total_asociados": asociados[0][0]
    }

def evaluate_rules(data):
    insights = []

    if data["transacciones_altas"] > 50:
        insights.append("Alto volumen de transacciones elevadas")

    if data["alertas_criticas"] > 20:
        insights.append("Número alto de alertas críticas")

    if data["total_asociados"] < 100:
        insights.append("Base de asociados baja")

    return insights


def generate_summary(data, insights):
    prompt = f"""
Eres un analista financiero.

Con base en estos datos:

- Transacciones altas: {data['transacciones_altas']}
- Alertas críticas: {data['alertas_criticas']}
- Total asociados: {data['total_asociados']}

Hallazgos:
{insights}

Genera un breve reporte claro y profesional con:
- Análisis general
- Posibles riesgos
- Recomendaciones
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

def run_monitoring(user):
    # 1. Obtener datos
    data = get_monitoring_data(user)

    print("\n Datos base:")
    print(data)

    # 2. Evaluar reglas
    insights = evaluate_rules(data)

    print("\n Insights detectados:")
    for i in insights:
        print("-", i)

    # 3. IA genera resumen
    summary = generate_summary(data, insights)

    return summary
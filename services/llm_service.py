# services/llm_service.py

import os
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def build_prompt(user_question: str):
    return f"""
    Eres un experto en SQL para SQLite.

    Convierte la siguiente pregunta en una consulta SQL válida.

    REGLAS:
    - La respuesta debe ser SOLO la consulta SQL, sin explicaciones ni texto adicional
    - No uses ``` ni formato markdown en la respuesta.
    - No incluyas explicaciones
    - Usa JOINs cuando sea necesario
    - SIEMPRE usa alias 'a' para la tabla asociados
    REGLA CRÍTICA:
    
    SIEMPRE debes hacer JOIN con la tabla asociados usando alias 'a'
    Ejemplo:
    JOIN asociados a ON ...

    ESQUEMA:

    Tabla asociados(id_asociado, nombre, apellido, ciudad, id_organizacion)
    Tabla cuentas(id_cuenta, id_asociado, tipo_cuenta, saldo)
    Tabla transacciones(id_transaccion, id_cuenta, tipo_transaccion, monto, fecha_transaccion)
    Tabla alertas(id_alerta, id_asociado, tipo_alerta, severidad, estado)

    Los valores de severidad en las alertas son exactamente:
    - Baja
    - Media
    - Alta
    - Critica


    RELACIONES:
    - cuentas.id_asociado → asociados.id_asociado
    - transacciones.id_cuenta → cuentas.id_cuenta
    - alertas.id_asociado → asociados.id_asociado

    Pregunta:
    {user_question}
    """

def call_llm(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Error Ollama: {response.text}")

    data = response.json()
    return data["response"]

def clean_sql(sql: str):
    # Quitar bloques tipo ```sql
    sql = sql.replace("```sql", "").replace("```", "")

    # Quitar texto antes del SELECT
    sql_upper = sql.upper()
    if "SELECT" in sql_upper:
        sql = sql[sql_upper.index("SELECT"):]

    # Quitar texto después del ;
    if ";" in sql:
        sql = sql.split(";")[0]

    return sql.strip()

### PRUEBA CON OPENROUTER

# OPENROUTER_API_KEY = ""
# assert OPENROUTER_API_KEY != ""
# def call_llm(prompt: str):
#     url = "https://openrouter.ai/api/v1/chat/completions"

#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     body = {
#         #"model": "openai/gpt-3.5-turbo",  # puedes cambiar modelo
#         #"model": "qwen/qwen3-4b:free",  # puedes cambiar modelo
#         "model": "google/gemma-3-4b-it:free",  # puedes cambiar modelo
#         "messages": [
#             {"role": "system", "content": "Eres un generador de SQL."},
#             {"role": "user", "content": prompt}
#         ],
#         "temperature": 0
#     }

#     response = requests.post(url, headers=headers, json=body)

#     if response.status_code != 200:
#         raise Exception(f"Error LLM: {response.text}")

#     data = response.json()

#     sql = data["choices"][0]["message"]["content"]

#     return sql.strip()


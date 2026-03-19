# services/nl_query_service.py

"""
Servicio de procesamiento de preguntas en lenguaje natural:
- Recibe una pregunta y el contexto del usuario (logged in)
- Construye un prompt para el LLM       
"""
from services.llm_service import build_prompt, call_llm, clean_sql
from services.query_builder import apply_org_filter
from services.query_executor import execute_query


def process_question(user, question: str):
    # 1. Crear prompt
    prompt = build_prompt(question)

    # 2. Llamar LLM
    raw_sql = call_llm(prompt)

    # print("\n SQL RAW:")
    # print(raw_sql)

    # 3. Limpiar SQL
    base_query = clean_sql(raw_sql)

    print("\n SQL generado:")
    print(base_query)

    # 4. Aplicar seguridad
    secure_query = apply_org_filter(base_query)

    # 5. Ejecutar
    results = execute_query(secure_query, (user.id_organizacion,))

    return results
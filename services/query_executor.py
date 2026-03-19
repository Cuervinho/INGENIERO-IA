# services/query_executor.py
"""
Ejecuta una consulta SQL con parámetros

- Recibe una consulta SQL y una tupla de parámetros
- Se conecta a la base de datos, ejecuta la consulta y devuelve los resultados  
"""

from db.connection import get_connection

def execute_query(query: str, params: tuple = ()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results
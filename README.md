# Engineer IA

## Descripción general

Este proyecto implementa una herramienta de análisis de datos financieros impulsada por Inteligencia Artificial. Permite a los usuarios autenticarse, consultar información mediante lenguaje natural y ejecutar procesos de monitoreo automatizado.

---

## Instrucciones de ejecución

1. Instalar dependencias:

pip install -r requirements.txt

2. Generar la base de datos:

python generar_base_datos.py

3. Ejecutar modelo local (Ollama):

ollama pull mistral
ollama run mistral

4. Ejecutar la aplicación:

python main.py

----------------

## Herramientas utilizadas

* Python
* SQLite
* Ollama
* Requests
* Matplotlib
* Github

---------------

## Decisiones de diseño

* IA local: uso de Ollama para evitar dependencias externas.
* Arquitectura modular
* Seguridad organizacional: se filtran los datos por organización del usuario que realiza la consulta.

----------------

## Posibles mejoras

* Usar OpenRouter para no depender de únicamente una IA local aportando flexibilidad de modelos.
* Realizar una interfaz web .
* Crear un sistema de alertas en tiempo real con notificacion al correo.
* Validación automática del SQL generado por la IA.


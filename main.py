# main.py

from auth.auth_service import login
from services.nl_query_service import process_question
from services.monitoring_service import run_monitoring

def main():
    print("=== LOGIN ===")

    username = input("Usuario: ")
    password = input("Password: ")

    user = login(username, password)

    if not user:
        print("❌ Login inválido")
        return

    print(f"\n✅ Bienvenido {user.username}")
    print(user)

    # Guardamos contexto (clave para todo el sistema)
    session = {"user": user}

    reporte = run_monitoring(user)
    print("\n REPORTE IA:\n")
    print(reporte)

    # while True:
    #     question = input("\nHaz una pregunta (o 'salir'): ")

    #     if question.lower() == "salir":
    #         break

    #     results = process_question(user, question)

    #     print("\n📊 Resultados:")
    #     for r in results[:10]:  # limit simple
    #         print(r)

if __name__ == "__main__":
    main()
from app.db import get_connection

def main():
    with get_connection as conn:
        print("Conectado correctamente")

if __name__ == "__main__":
    main()
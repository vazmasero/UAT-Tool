import sqlite3
import os


def open_db_shell():
    db_path = "uat_tool.db"

    if not os.path.exists(db_path):
        print(f"Base de datos no encontrada en: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Para obtener resultados como diccionarios

    print(f"Conectado a: {db_path}")
    print("Comandos disponibles:")
    print("  tables - Ver todas las tablas")
    print("  schema <tabla> - Ver estructura de tabla")
    print("  drop bugs - Eliminar tabla bugs")
    print("  drop uspaces - Eliminar tabla uspaces")
    print("  drop cases - Eliminar tabla cases")
    print("  drop blocks - Eliminar tabla blocks")
    print("  drop all - Eliminar todas las tablas")
    print("  create uspaces - Crear tabla uspaces")
    print("  exit - Salir")

    while True:
        try:
            command = input("\nsqlite> ").strip().lower()

            if command == "exit":
                break
            elif command == "tables":
                cursor = conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'")
                tables = cursor.fetchall()
                print("Tablas:")
                for table in tables:
                    print(f"  - {table[0]}")
            elif command.startswith("schema"):
                parts = command.split()
                if len(parts) > 1:
                    table = parts[1]
                    cursor = conn.execute(
                        f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table}'")
                    result = cursor.fetchone()
                    if result:
                        print(f"Estructura de {table}:")
                        print(result[0])
                    else:
                        print(f"Tabla '{table}' no encontrada")
                else:
                    print("Uso: schema <nombre_tabla>")
            elif command == "drop bugs":
                conn.execute("DROP TABLE IF EXISTS bugs")
                conn.commit()
                print("Tabla bugs eliminada")
            elif command == "drop uspaces":
                conn.execute("DROP TABLE IF EXISTS uspaces")
                conn.commit()
                print("Tabla uspaces eliminada")
            elif command == "drop cases":
                conn.execute("DROP TABLE IF EXISTS cases")
                conn.commit()
                print("Tabla cases eliminada")
            elif command == "drop blocks":
                conn.execute("DROP TABLE IF EXISTS blocks")
                conn.commit()
                print("Tabla blocks eliminada")
            elif command == "drop all":
                # Obtener todas las tablas
                cursor = conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'")
                tables = cursor.fetchall()

                if not tables:
                    print("No hay tablas para eliminar")
                else:
                    confirm = input(
                        f"¿Estás seguro de que quieres eliminar todas las {len(tables)} tablas? (y/N): ").strip().lower()
                    if confirm in ['y', 'yes', 'si', 's']:
                        for table in tables:
                            conn.execute(f"DROP TABLE IF EXISTS {table[0]}")
                            print(f"  - Tabla {table[0]} eliminada")
                        conn.commit()
                        print("Todas las tablas han sido eliminadas")
                    else:
                        print("Operación cancelada")
            elif command == "create uspaces":
                conn.execute("""
                    CREATE TABLE uspaces (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        identification VARCHAR NOT NULL,
                        name VARCHAR NOT NULL,
                        sectors_number INTEGER NOT NULL,
                        file TEXT,
                        creation_time DATETIME,
                        last_update DATETIME
                    )
                """)
                conn.commit()
                print("Tabla uspaces creada")
            else:
                # Ejecutar SQL directo
                try:
                    cursor = conn.execute(command)
                    if cursor.description:  # Si retorna resultados
                        results = cursor.fetchall()
                        for row in results:
                            print(dict(row))
                    conn.commit()
                    print("Comando ejecutado correctamente")
                except sqlite3.Error as e:
                    print(f"Error SQL: {e}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

    conn.close()
    print("Desconectado")


if __name__ == "__main__":
    open_db_shell()

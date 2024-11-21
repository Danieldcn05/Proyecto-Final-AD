import sqlite3
import os

def create_database(db_name="app_database.db"):
    if not os.path.exists(db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Crear una tabla de ejemplo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        
        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        print(f"Database '{db_name}' created successfully.")
    else:
        print(f"Database '{db_name}' already exists.")



def insert_user(name, email, db_name="app_database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Insertar un nuevo usuario
    try:
        cursor.execute('''
            INSERT INTO users (name, email) VALUES (?, ?)
        ''', (name, email))
        
        # Guardar los cambios
        conn.commit()
        print(f"User {name} inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting user: {e}")
    finally:
        # Cerrar la conexión
        conn.close()



if __name__ == "__main__":
    create_database()
    insert_user("Carmen Sanchez", "carmen@gmail.com")
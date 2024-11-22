import sqlite3
import os

def create_database(db_name="app_database.db"):
    if not os.path.exists(db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_apel TEXT,
                fec_ini DATE,
                fec_nac DATE,
                fec_baja DATE,
                dir TEXT,
                nif TEXT,
                dat_banc TEXT,
                num_ss TEXT,
                gen TEXT,
                depart TEXT,
                puesto TEXT,
                tlf TEXT,
                email TEXT,
                sal_men REAL,
                pag_ext REAL,
                por_irpf REAL,
                por_ss REAL
            )
        ''')
        
        
        conn.commit()
        conn.close()
        print(f"Database '{db_name}' created successfully.")
    else:
        print(f"Database '{db_name}' already exists.")



def insert_empleado(nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss, db_name="app_database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Insertar un nuevo empleado
    try:
        cursor.execute('''
            INSERT INTO empleados (nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss))
        
        # Guardar los cambios
        conn.commit()
        print(f"Empleado {nom_apel} insertado exitosamente.")
    except sqlite3.IntegrityError as e:
        print(f"Error al insertar empleado: {e}")
    finally:
        # Cerrar la conexión
        conn.close()


def asignar_fec_baja(emp_id, fec_baja, db_name="app_database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            UPDATE empleados
            SET fec_baja = ?
            WHERE id = ?
        ''', (fec_baja, emp_id))
        
        # Guardar los cambios
        conn.commit()
        print(f"Fecha de baja {fec_baja} asignada exitosamente al empleado con ID {emp_id}.")
    except sqlite3.Error as e:
        print(f"Error al asignar fecha de baja: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == "__main__":
    create_database()
    insert_empleado(
        "Carmen Sanchez", "2023-01-01", "1990-05-15", "Calle Falsa 123", "12345678A", "ES7620770024003102575766", "123456789", "F", "Ventas", "Gerente", "123456789", "carmen@gmail.com", 3000.0, 500.0, 15.0, 6.35
    )
    
    asignar_fec_baja(1, "2023-01-01")
import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="app_database.db"):
        self.db_name = db_name

    def create_database(self):
        if not os.path.exists(self.db_name):
            conn = sqlite3.connect(self.db_name)
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
            print(f"Database '{self.db_name}' created successfully.")
        else:
            print(f"Database '{self.db_name}' already exists.")

    def insert_empleado(self, nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO empleados (nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss))
            
            conn.commit()
            print(f"Empleado {nom_apel} insertado exitosamente.")
        except sqlite3.IntegrityError as e:
            print(f"Error al insertar empleado: {e}")
        finally:
            conn.close()

    def asignar_fec_baja(self, emp_id, fec_baja):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                UPDATE empleados
                SET fec_baja = ?
                WHERE id = ?
            ''', (fec_baja, emp_id))
            
            conn.commit()
            print(f"Fecha de baja {fec_baja} asignada exitosamente al empleado con ID {emp_id}.")
        except sqlite3.Error as e:
            print(f"Error al asignar fecha de baja: {e}")
        finally:
            conn.close()

    def usuario_existe(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM empleados WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        
        conn.close()
        
        return result is not None 
    
    def tiene_fecha_baja(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT fec_baja FROM empleados WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result is None:
            return False  # El usuario no existe
        return result[0] is not None  # True si tiene fecha de baja, False si es NULL
    
    def get_empleado(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM empleados WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        
        conn.close()
        
        return result
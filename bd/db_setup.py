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
            self.insert_example_employees()
        else:
            print(f"Database '{self.db_name}' already exists.")
            
            
    def insert_example_employees(self):
        example_employees = [
            ("Juan Pérez", "2021-01-01", "1985-05-15", "Calle Falsa 123", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "Ventas", "Vendedor", "123456789", "juan.perez@example.com", 2000.0, 1, 15.0, 6.35),
            ("Ana García", "2021-02-01", "1990-07-20", "Avenida Siempre Viva 742", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Marketing", "Analista", "234567890", "ana.garcia@example.com", 2200.0, 2, 14.0, 6.35),
            ("Luis Martínez", "2021-03-01", "1982-03-10", "Calle Luna 456", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "IT", "Desarrollador", "345678901", "luis.martinez@example.com", 2500.0, 3, 18.0, 6.35),
            ("María López", "2021-04-01", "1988-11-25", "Calle Sol 789", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Recursos Humanos", "Gerente", "456789012", "maria.lopez@example.com", 2400.0, 1, 16.0, 6.35),
            ("Carlos Sánchez", "2021-05-01", "1975-09-30", "Calle Estrella 101", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "Finanzas", "Contador", "567890123", "carlos.sanchez@example.com", 2300.0, 2, 17.0, 6.35),
            ("Laura Fernández", "2021-06-01", "1995-12-05", "Calle Cometa 202", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Ventas", "Vendedor", "678901234", "laura.fernandez@example.com", 2100.0, 3, 15.0, 6.35),
            ("Jorge Gómez", "2021-07-01", "1983-08-15", "Calle Planeta 303", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "IT", "Administrador", "789012345", "jorge.gomez@example.com", 2600.0, 1, 19.0, 6.35),
            ("Elena Ruiz", "2021-08-01", "1992-04-10", "Calle Galaxia 404", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Marketing", "Especialista", "890123456", "elena.ruiz@example.com", 2250.0, 2, 14.5, 6.35),
            ("Pedro Ramírez", "2021-09-01", "1987-06-20", "Calle Universo 505", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "Recursos Humanos", "Asistente", "901234567", "pedro.ramirez@example.com", 2050.0, 3, 13.0, 6.35),
            ("Sofía Torres", "2021-10-01", "1993-10-25", "Calle Constelación 606", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Finanzas", "Analista", "012345678", "sofia.torres@example.com", 2350.0, 1, 16.5, 6.35),
            ("Miguel Ángel", "2021-11-01", "1980-01-15", "Calle del Sol 123", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "Logística", "Supervisor", "112233445", "miguel.angel@example.com", 2700.0, 2, 20.0, 6.35),
            ("Lucía Martínez", "2021-12-01", "1991-03-22", "Calle de la Luna 456", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Ventas", "Representante", "223344556", "lucia.martinez@example.com", 2100.0, 3, 15.0, 6.35),
            ("David Fernández", "2022-01-01", "1984-07-30", "Calle de las Estrellas 789", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "IT", "Ingeniero", "334455667", "david.fernandez@example.com", 2800.0, 1, 21.0, 6.35),
            ("Isabel Gómez", "2022-02-01", "1989-09-10", "Calle de los Planetas 101", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Marketing", "Coordinadora", "445566778", "isabel.gomez@example.com", 2300.0, 2, 16.0, 6.35),
            ("Fernando Ruiz", "2022-03-01", "1978-11-25", "Calle de las Galaxias 202", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "Recursos Humanos", "Director", "556677889", "fernando.ruiz@example.com", 3000.0, 3, 22.0, 6.35),
            ("Patricia Ramírez", "2022-04-01", "1994-05-05", "Calle del Universo 303", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Finanzas", "Contadora", "667788990", "patricia.ramirez@example.com", 2400.0, 1, 17.0, 6.35),
            ("Alberto Torres", "2022-05-01", "1986-12-12", "Calle de la Constelación 404", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "Logística", "Operador", "778899001", "alberto.torres@example.com", 2200.0, 2, 15.0, 6.35),
            ("Marta López", "2022-06-01", "1992-08-18", "Calle del Cometa 505", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Ventas", "Asistente", "889900112", "marta.lopez@example.com", 2000.0, 3, 14.0, 6.35),
            ("Raúl Sánchez", "2022-07-01", "1981-02-28", "Calle del Meteorito 606", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "M", "IT", "Técnico", "990011223", "raul.sanchez@example.com", 2500.0, 1, 18.0, 6.35),
            ("Sara Torres", "2022-08-01", "1990-06-15", "Calle del Asteroide 707", "12345678Z", "ES24 0528 6704 73 7978721006", "43/08308793/34", "F", "Marketing", "Asistente", "001122334", "sara.torres@example.com", 2200.0, 2, 15.0, 6.35)
        ]
    
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
    
        cursor.executemany('''
            INSERT INTO empleados (nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', example_employees)
    
        conn.commit()
        conn.close()
        print("20 empleados de ejemplo insertados exitosamente.")

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
    
    def get_total_empleados(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM empleados WHERE fec_baja IS NULL")
        result = cursor.fetchone()
        
        conn.close()
        
        return result[0] if result else 0
    
    def get_total_hombres(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM empleados WHERE gen = 'M' AND fec_baja IS NULL")
        result = cursor.fetchone()
        
        conn.close()
        
        return result[0] if result else 0
    
    def get_total_bajas(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM empleados WHERE fec_baja IS NOT NULL")
        result = cursor.fetchone()
        
        conn.close()
        
        return result[0] if result else 0
    
    def get_total_hom_bajas(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM empleados WHERE gen = 'M' AND fec_baja IS NOT NULL")
        result = cursor.fetchone()
        
        conn.close()
        
        return result[0] if result else 0
    
    def get_media_edad(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
    
        # Calcular la edad media de los hombres
        cursor.execute("""
            SELECT AVG((julianday('now') - julianday(fec_nac)) / 365.25) 
            FROM empleados 
            WHERE gen = 'M'
            AND fec_baja IS NULL
        """)
        media_edad_hombres = cursor.fetchone()[0]
        if media_edad_hombres is None:
            media_edad_hombres = 0
    
        # Calcular la edad media de las mujeres
        cursor.execute("""
            SELECT AVG((julianday('now') - julianday(fec_nac)) / 365.25) 
            FROM empleados 
            WHERE gen = 'F'
            AND fec_baja IS NULL
        """)
        media_edad_mujeres = cursor.fetchone()[0]
        if media_edad_mujeres is None:
            media_edad_mujeres = 0
    
        conn.close()
    
        return media_edad_hombres, media_edad_mujeres
    
    def get_media_salario(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Calcular el salario mensual medio de los hombres
        cursor.execute("""
            SELECT AVG(sal_men) 
            FROM empleados 
            WHERE gen = 'M'
            AND fec_baja IS NULL
        """)
        media_salario_hombres = cursor.fetchone()[0]
        if media_salario_hombres is None:
            media_salario_hombres = 0

        # Calcular el salario mensual medio de las mujeres
        cursor.execute("""
            SELECT AVG(sal_men) 
            FROM empleados 
            WHERE gen = 'F'
            AND fec_baja IS NULL
        """)
        media_salario_mujeres = cursor.fetchone()[0]
        if media_salario_mujeres is None:
            media_salario_mujeres = 0

        conn.close()

        return media_salario_hombres, media_salario_mujeres
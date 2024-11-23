from bd.db_setup import DatabaseManager
import re
from datetime import datetime


class EmpleadoManager:
        def __init__(self):
            self.db_manager = DatabaseManager()

        def validate_employee_data(self, fec_ini, fec_nac, nif, dat_banc, num_ss, gen, email, sal_men, msg_val):
            # Validar fechas
            try:
                datetime.strptime(fec_ini, '%Y-%m-%d')
                datetime.strptime(fec_nac, '%Y-%m-%d')
            except ValueError:
                msg_val.config(text="FORMATO DE FECHA INVÁLIDO (AAAA-MM-DD)", fg="red")
                raise ValueError("Formato de fecha inválido")

            # Validar NIF
            if not self.validar_nif(nif):
                msg_val.config(text="NIF INVÁLIDO", fg="red")
                raise ValueError("NIF inválido")

            # Validar email
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                msg_val.config(text="EMAIL INVÁLIDO (empleado@gmail.com)", fg="red")
                raise ValueError("Email inválido")

            if not self.validar_ccc(dat_banc):
                msg_val.config(text="CCC INVÁLIDO (ESXX XXXX XXXX XX XXXXXXXXXX)", fg="red")
                raise ValueError("CCC inválido")
            
            if not self.validar_naf(num_ss):
                msg_val.config(text="Nº SS INVÁLIDO", fg="red")
                raise ValueError("Numero seguridad social inválido")
            
            if gen != "F" and gen != "M":
                msg_val.config(text="GÉNERO INVÁLIDO (F o M)", fg="red")
                raise ValueError("Género inválido")
            
            if int(sal_men) < 0:
                msg_val.config(text="SALARIO MENSUAL INVÁLIDO", fg="red")
                raise ValueError("Salario mensual inválido")
            
            return True
            

        def add_employee(self, nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss, msg_val):
            if self.validate_employee_data(fec_ini, fec_nac, nif, dat_banc, num_ss, gen, email, sal_men,msg_val):
                self.db_manager.insert_empleado(nom_apel, fec_ini, fec_nac, dir, nif, dat_banc, num_ss, gen, depart, puesto, tlf, email, sal_men, pag_ext, por_irpf, por_ss)
                msg_val.config(text="Empleado insertado exitosamente", fg="green")
                return True
            else:
                return False

        def validar_nif(self, nif):
                numeros, letra = self.separar_numeros_letra(nif)
                if numeros is None or letra is None:
                    return False

                numeros = int(numeros)
                letras = "TRWAGMYFPDXBNJZSQVHLCKE"

                if len(nif) == 9:
                    n1 = numeros // 23  # División entera
                    n2 = n1 * 23
                    resultado = numeros - n2

                    if letra == letras[resultado]:
                        return True
                    else:
                        return False
                else:
                    return False

        def separar_numeros_letra(self, cadena):
            match = re.match(r"(\d+)([A-Z])", cadena, re.I) 
            if match:
                numeros = match.group(1)
                letra = match.group(2)
                return numeros, letra
            else:
                return None, None
        
        def validar_naf(self, naf):
            partes = naf.split("/")
            
            if len(partes) != 3:
                return False
            try:
                a = int(partes[0])
                b = int(partes[1])
                c = int(partes[2])
            except ValueError:
                return False

            if b < 10000000:
                resultado = (b + a * 10000000) % 97
            else:
                concat = str(a) + str(b)
                resultado = (int(concat) % 97)
            
            return resultado == c
        def validar_ccc(self,ccc):
            if len(ccc) != 28:
                return False

            partes = ccc.split(" ")

            iban = partes[0]
            entidad = partes[1]
            sucursal = partes[2]
            control = partes[3]
            codigo = partes[4]

            digito1 = 11 - (((int(entidad[0]) * 4) + (int(entidad[1]) * 8) + (int(entidad[2]) * 5) + (int(entidad[3]) * 10) + (int(sucursal[0]) * 9) + (int(sucursal[1]) * 7) + (int(sucursal[2]) * 3) + (int(sucursal[3]) * 6)) % 11)

            if digito1 == 10:
                digito1 = 1

            digito2 = 11 - (((int(codigo[0]) * 1) + (int(codigo[1]) * 2) + (int(codigo[2]) * 4) + (int(codigo[3]) * 8) + (int(codigo[4]) * 5) + (int(codigo[5]) * 10) + (int(codigo[6]) * 9) + (int(codigo[7]) * 7) + (int(codigo[8]) * 3) + (int(codigo[9]) * 6)) % 11)

            # Validar los dígitos de control
            if int(control[0]) != digito1 or int(control[1]) != digito2:
                return False
            
            
            # Calcular el IBAN
            numero_cuenta_completo = entidad + sucursal + control + codigo
            numero_iban = numero_cuenta_completo + "142800"
            resto = int(numero_iban) % 97
            digito_control_iban = 98 - resto
            iban = "ES" + str(digito_control_iban).zfill(2)

            if iban == partes[0] and str(digito1) == control[0] and str(digito2) == control[1]:
                return True
            else:
                return False
            
        def asignar_fec_baja(self, emp_id, fec_baja, msg_val):

            try:
                datetime.strptime(fec_baja, '%Y-%m-%d')
            except ValueError:
                msg_val.config(text="FORMATO DE FECHA INVÁLIDO (AAAA-MM-DD)", fg="red")
                raise ValueError("Formato de fecha inválido")

            if self.db_manager.usuario_existe(emp_id) and not self.db_manager.tiene_fecha_baja(emp_id):
                self.db_manager.asignar_fec_baja(emp_id, fec_baja)
                msg_val.config(text="EMPLEADO DADO DE BAJA EXITOSAMENTE", fg="green")
                return True
            else:
                msg_val.config(text="EMPLEADO NO EXISTE", fg="red")
                return False
            
           
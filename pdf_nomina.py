from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Nómina', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def employee_info(self, name,direccion,nif, ccc, num_ss):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Información del Empleado', 0, 1)
        
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Nombre: {name}', 0, 1)
        self.cell(0, 10, f'Dirección: {direccion}', 0, 1)
        self.cell(0, 10, f'Número de Identificación: {nif}', 0, 1)
        self.cell(0, 10, f'Número de Seguridad Social: {num_ss}', 0, 1)
        self.cell(0, 10, f'Cuenta Bancaria: {ccc}', 0, 1)
        
        self.ln(10)

    def salary_details(self, salary_bruto, salario_neto,num_pagas, por_irpf, por_ss, ret_irpf, ret_ss):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Detalles del Salario', 0, 1)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Salario Bruto: {salary_bruto} EUR', 0, 1)
        self.cell(0, 10, f'Número de Pagas: {num_pagas}', 0, 1)
        self.cell(0, 10, f'Porcentaje de IRPF: {por_irpf}%', 0, 1)
        self.cell(0, 10, f'Retención IRPF: {ret_irpf} EUR', 0, 1)
        self.cell(0, 10, f'Porcentaje de Seguridad Social: {por_ss}%', 0, 1)
        self.cell(0, 10, f'Retención Seguridad Social: {ret_ss} EUR', 0, 1)
        self.cell(0, 10, f'Salario Neto: {salario_neto} EUR', 0, 1)
        self.ln(10)

    def generar_pdf(self,nombre, direccion, nif, ccc, num_ss, salario_bruto, salario_neto, num_pagas, por_irpf, por_ss, ret_irpf, ret_ss):
        # Crear una instancia de PDF
        pdf = PDF()

        # Agregar una página
        pdf.add_page()

        # Información del empleado
        pdf.employee_info(nombre, direccion, nif, ccc, num_ss)

        # Detalles del salario
        pdf.salary_details(salario_bruto, salario_neto, num_pagas, por_irpf, por_ss, ret_irpf, ret_ss)
        
        # Crear una ventana de Tkinter (no visible)
        root = tk.Tk()
        root.withdraw()

        # Abrir el cuadro de diálogo de guardado de archivos
        ruta_archivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        # Generar el PDF si se seleccionó una ruta
        if ruta_archivo:
            # Guardar el PDF
            pdf.output(ruta_archivo)


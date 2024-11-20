import tkinter as tk
from tkinter import Label, Button, Entry

class View2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

       
        estilo_boton = {
            "width": 20,
            "height": 2,
            "bg": "#FFE781",
            "fg": "black",
            "font": ("Helvetica", 16, "bold"),
            "relief": "solid",
            "bd": 2,  
            "activebackground": "#E2CD6D", 
            "activeforeground": "black",
        }

        # Configuración filas y columnas
        num_filas = 11
        num_columnas = 6
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)
        ############################################
        
        Label(self, text="NOMBRE Y APELLIDOS").grid(row=0, column=0, columnspan=6)
        Entry(self).grid(row=1, column=0, columnspan=6)
        
        Label(self, text="FECHA INICIO").grid(row=2, column=0)
        Entry(self).grid(row=3, column=0)

        Label(self, text="FECHA NACIMIENTO").grid(row=2, column=1)
        Entry(self).grid(row=3, column=1)

        Label(self, text="DIRECCIÓN").grid(row=2, column=2)
        Entry(self).grid(row=3, column=2)

        Label(self, text="NIF").grid(row=4, column=0)
        Entry(self).grid(row=5, column=0)

        Label(self, text="DATOS BANCARIOS").grid(row=4, column=1)
        Entry(self).grid(row=5, column=1)

        Label(self, text="NUMERO DE AFILIACIÓN SS").grid(row=4, column=2)
        Entry(self).grid(row=5, column=2)

        Label(self, text="GÉNERO").grid(row=6, column=0)
        Entry(self).grid(row=7, column=0)

        Label(self, text="DEPARTAMENTO").grid(row=6, column=1)
        Entry(self).grid(row=7, column=1)

        Label(self, text="PUESTO").grid(row=6, column=2)
        Entry(self).grid(row=7, column=2)

        Label(self, text="TELEFONO").grid(row=8, column=0)
        Entry(self).grid(row=8, column=1)

        Label(self, text="SALARIO MENSUAL").grid(row=8, column=2)
        Entry(self).grid(row=8, column=3)

        Label(self, text="IRPF").grid(row=8, column=4)
        Entry(self).grid(row=8, column=5)

        Label(self, text="EMAIL").grid(row=9, column=0)
        Entry(self).grid(row=9, column=1)

        Label(self, text="PAGAS EXTRA").grid(row=9, column=2)
        Entry(self).grid(row=9, column=3)

        Label(self, text="SEG. SOCIAL").grid(row=9, column=4)
        Entry(self).grid(row=9, column=5)

        Label(self, text="MENSAJES VALIDACIÓN").grid(row=10, column=0, columnspan=4)

        Button(self, text="INSERTAR", **estilo_boton).grid(row=10, column=5)


        

       # Button(self, text="Back to View 1", **estilo_boton, command=lambda: controller.show_frame("View1")).grid(row=2, column=1, columnspan=2)
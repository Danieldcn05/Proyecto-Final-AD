import tkinter as tk
from tkinter import Label, Button, Entry, PhotoImage
from empleado_manager import EmpleadoManager

class View2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.empleado_manager = EmpleadoManager()
                                             
        

        self.back_img = PhotoImage(file="assets\\back.png").subsample(10)
       
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
        
        estilo_label = {
            "fg": "black",
            "font": ("Helvetica", 12, "bold")
        }

        estilo_entry = {
            "font": ("Helvetica", 12),
            "bd": 1,
            "relief": "solid"
           
        }
        
        # Configuración filas y columnas
        num_filas = 11
        num_columnas = 6
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)
        ############################################
        
        Label(self, text="NOMBRE Y APELLIDOS", **estilo_label).grid(row=0, column=0, columnspan=6, pady=(5, 5))
        self.nombre_apel_entry = Entry(self, **estilo_entry)
        self.nombre_apel_entry.grid(row=1, column=0, columnspan=6, sticky="ew", padx=100, ipady=6)

        Label(self, text="FECHA INICIO", **estilo_label).grid(row=2, column=0, columnspan=1, padx=(100, 25))
        self.fec_ini_entry = Entry(self, **estilo_entry)
        self.fec_ini_entry.grid(row=3, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="FECHA NACIMIENTO", **estilo_label).grid(row=2, column=1, columnspan=1, padx=(25, 25))
        self.fec_nac_entry = Entry(self, **estilo_entry)
        self.fec_nac_entry.grid(row=3, column=1, columnspan=1, sticky="ew", padx=(25, 25), ipady=6)

        Label(self, text="DIRECCIÓN", **estilo_label).grid(row=2, column=2, columnspan=4, padx=(25, 100))
        self.direccion_entry = Entry(self, **estilo_entry)
        self.direccion_entry.grid(row=3, column=2, columnspan=4, sticky="ew", padx=(25, 100), ipady=6)

        Label(self, text="NIF", **estilo_label).grid(row=4, column=0, columnspan=1, padx=(100, 25), sticky="ew")
        self.nif_entry = Entry(self, **estilo_entry)
        self.nif_entry.grid(row=5, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="DATOS BANCARIOS", **estilo_label).grid(row=4, column=1, columnspan=3, padx=(25, 25), sticky="ew")
        self.datos_bancarios_entry = Entry(self, **estilo_entry)
        self.datos_bancarios_entry.grid(row=5, column=1, columnspan=3, sticky="ew", padx=(25, 25), ipady=6)

        Label(self, text="NUMERO DE AFILIACIÓN SS", **estilo_label).grid(row=4, column=4, columnspan=2, padx=(25, 100), sticky="ew")
        self.num_afiliacion_entry = Entry(self, **estilo_entry)
        self.num_afiliacion_entry.grid(row=5, column=4, columnspan=2, sticky="ew", padx=(25, 100), ipady=6)

        Label(self, text="GÉNERO", **estilo_label).grid(row=6, column=0, columnspan=1, padx=(100, 25), sticky="ew")
        self.genero_entry = Entry(self, **estilo_entry)
        self.genero_entry.grid(row=7, column=0, columnspan=1, padx=(100, 25), sticky="ew", ipady=6)

        Label(self, text="DEPARTAMENTO", **estilo_label).grid(row=6, column=1, columnspan=3, padx=(25, 25), sticky="ew")
        self.departamento_entry = Entry(self, **estilo_entry)
        self.departamento_entry.grid(row=7, column=1, columnspan=3, padx=(25, 25), sticky="ew", ipady=6)

        Label(self, text="PUESTO", **estilo_label).grid(row=6, column=4, columnspan=2, padx=(25, 100), sticky="ew")
        self.puesto_entry = Entry(self, **estilo_entry)
        self.puesto_entry.grid(row=7, column=4, columnspan=2, padx=(25, 100), sticky="ew", ipady=6)

        Label(self, text="TELEFONO", anchor="w", **estilo_label).grid(row=8, column=0, sticky="ew", padx=(100, 0))
        self.telefono_entry = Entry(self, **estilo_entry)
        self.telefono_entry.grid(row=8, column=1, sticky="ew", ipady=6)

        Label(self, text="SALARIO MENSUAL", anchor="w", **estilo_label).grid(row=8, column=2, sticky="ew", padx=(50, 25))
        self.salario_entry = Entry(self, **estilo_entry)
        self.salario_entry.grid(row=8, column=3, sticky="ew", ipady=6)

        Label(self, text="IRPF", anchor="w", **estilo_label).grid(row=8, column=4, sticky="ew", padx=(50, 25))
        self.irpf_entry = Entry(self, **estilo_entry)
        self.irpf_entry.grid(row=8, column=5, sticky="ew", padx=(0, 100), ipady=6)

        Label(self, text="EMAIL", anchor="w", **estilo_label).grid(row=9, column=0, sticky="ew", padx=(100, 0))
        self.email_entry = Entry(self, **estilo_entry)
        self.email_entry.grid(row=9, column=1, sticky="ew", ipady=6)

        Label(self, text="PAGAS EXTRA", anchor="w", **estilo_label).grid(row=9, column=2, sticky="ew", padx=(50, 25))
        self.pagas_extra_entry = Entry(self, **estilo_entry)
        self.pagas_extra_entry.grid(row=9, column=3, sticky="ew", ipady=6)

        Label(self, text="SS", anchor="w", **estilo_label).grid(row=9, column=4, sticky="ew", padx=(50, 25))
        self.ss_entry = Entry(self, **estilo_entry)
        self.ss_entry.grid(row=9, column=5, sticky="ew", padx=(0, 100), ipady=10)

        self.msg_val = Label(self, text="MENSAJES VALIDACIÓN", font=("Helvetica",18,"bold"), fg="red", bd=1, relief="solid")
        self.msg_val.grid(row=10, column=0, columnspan=4, sticky="ew", padx=(100,0), ipady=10)
        

        Button(self, text="INSERTAR", **estilo_boton, command=self.validate_entries).grid(row=10, column=5, columnspan=2, padx=(0, 100))

    


        Button(self, image=self.back_img,bd=0, command=lambda: controller.show_frame("View1")).place(x=10, y=10)


    def validate_entries(self):
            entries = [
                self.nombre_apel_entry,
                self.fec_ini_entry,
                self.fec_nac_entry,
                self.direccion_entry,
                self.nif_entry,
                self.datos_bancarios_entry,
                self.num_afiliacion_entry,
                self.genero_entry,
                self.departamento_entry,
                self.puesto_entry,
                self.telefono_entry,
                self.email_entry,
                self.salario_entry,
                self.pagas_extra_entry,
                self.irpf_entry,
                self.ss_entry
            ]

            for entry in entries:
                if not entry.get():
                    self.msg_val.config(text="NO SE PUEDEN DEJAR CAMPOS VACIOS", fg="red")
                    return

            if  self.empleado_manager.add_employee(
                self.nombre_apel_entry.get(),
                self.fec_ini_entry.get(),
                self.fec_nac_entry.get(),
                self.direccion_entry.get(),
                self.nif_entry.get(),
                self.datos_bancarios_entry.get(),
                self.num_afiliacion_entry.get(),
                self.genero_entry.get(),
                self.departamento_entry.get(),
                self.puesto_entry.get(),
                self.telefono_entry.get(),
                self.email_entry.get(),
                self.salario_entry.get(),
                self.pagas_extra_entry.get(),
                self.irpf_entry.get(),
                self.ss_entry.get(),
                self.msg_val
            ):
                 for entry in entries:
                    entry.delete(0, "end")
           

            

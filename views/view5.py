import tkinter as tk
from tkinter import Label, Button, PhotoImage, Entry
from empleado_manager import EmpleadoManager
from bd.db_setup import DatabaseManager
from pdf_nomina import PDF

class View5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.empleado_manager = EmpleadoManager()
        self.db_manager = DatabaseManager()
        self.pdf = PDF()

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
            "relief": "solid",
            "disabledbackground": "#caf0f8",
        }

        # Configuración filas y columnas
        num_filas = 11
        num_columnas = 6
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)
        ############################################

        # Variables StringVar para los Entry
        self.codigo_var = tk.StringVar()
        self.nombre_apellidos_var = tk.StringVar()
        self.fecha_inicio_var = tk.StringVar()
        self.fecha_nacimiento_var = tk.StringVar()
        self.direccion_var = tk.StringVar()
        self.nif_var = tk.StringVar()
        self.datos_bancarios_var = tk.StringVar()
        self.num_afiliacion_ss_var = tk.StringVar()
        self.salario_bruto_var = tk.StringVar()
        self.numero_pagas_var = tk.StringVar()
        self.salario_mes_var = tk.StringVar()
        self.irpf_var = tk.StringVar()
        self.retencion_irpf_var = tk.StringVar()
        self.prorrata_pagas_var = tk.StringVar()
        self.seg_social_var = tk.StringVar()
        self.deduccion_ss_var = tk.StringVar()
        self.a_percibir_var = tk.StringVar()

        Label(self, text="CÓDIGO", **estilo_label).grid(row=0, column=0, columnspan=1, padx=(100, 0))
        codigo_entry = Entry(self, textvariable=self.codigo_var, **estilo_entry)
        codigo_entry.grid(row=1, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="NOMBRE Y APELLIDOS", **estilo_label).grid(row=0, column=1, columnspan=5)
        nombre_apellidos_entry = Entry(self, textvariable=self.nombre_apellidos_var, **estilo_entry, state="disabled")
        nombre_apellidos_entry.grid(row=1, column=1, columnspan=5, sticky="ew", padx=(25, 100), ipady=6)

        Label(self, text="FECHA INICIO", **estilo_label).grid(row=2, column=0, columnspan=1, padx=(100, 25))
        fecha_inicio_entry = Entry(self, textvariable=self.fecha_inicio_var, **estilo_entry, state="disabled")
        fecha_inicio_entry.grid(row=3, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="FECHA NACIMIENTO", **estilo_label).grid(row=2, column=1, columnspan=1, padx=(25, 25))
        fecha_nacimiento_entry = Entry(self, textvariable=self.fecha_nacimiento_var, **estilo_entry, state="disabled")
        fecha_nacimiento_entry.grid(row=3, column=1, columnspan=1, sticky="ew", padx=(25, 25), ipady=6)

        Label(self, text="DIRECCIÓN", **estilo_label).grid(row=2, column=2, columnspan=4, padx=(25, 100))
        direccion_entry = Entry(self, textvariable=self.direccion_var, **estilo_entry, state="disabled")
        direccion_entry.grid(row=3, column=2, columnspan=4, sticky="ew", padx=(25, 100), ipady=6)

        Label(self, text="NIF", **estilo_label).grid(row=4, column=0, columnspan=1, padx=(100, 25), sticky="ew")
        nif_entry = Entry(self, textvariable=self.nif_var, **estilo_entry, state="disabled")
        nif_entry.grid(row=5, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="DATOS BANCARIOS", **estilo_label).grid(row=4, column=1, columnspan=3, padx=(25, 25), sticky="ew")
        datos_bancarios_entry = Entry(self, textvariable=self.datos_bancarios_var, **estilo_entry, state="disabled")
        datos_bancarios_entry.grid(row=5, column=1, columnspan=3, sticky="ew", padx=(25, 25), ipady=6)

        Label(self, text="NUMERO DE AFILIACIÓN SS", **estilo_label).grid(row=4, column=4, columnspan=2, padx=(25, 100), sticky="ew")
        num_afiliacion_ss_entry = Entry(self, textvariable=self.num_afiliacion_ss_var, **estilo_entry, state="disabled")
        num_afiliacion_ss_entry.grid(row=5, column=4, columnspan=2, sticky="ew", padx=(25, 100), ipady=6)

        Label(self, text="SALARIO BRUTO", anchor="w", **estilo_label).grid(row=6, column=0, sticky="ew", padx=(100, 0))
        salario_bruto_entry = Entry(self, textvariable=self.salario_bruto_var, **estilo_entry, state="disabled")
        salario_bruto_entry.grid(row=6, column=1, sticky="ew", ipady=6)

        Label(self, text="NUMERO PAGAS", anchor="w", **estilo_label).grid(row=6, column=2, sticky="ew", padx=(50, 25))
        numero_pagas_entry = Entry(self, textvariable=self.numero_pagas_var, **estilo_entry, state="disabled")
        numero_pagas_entry.grid(row=6, column=3, sticky="ew", ipady=6)

        Label(self, text="SALARIO MES", anchor="w", **estilo_label).grid(row=7, column=0, sticky="ew", padx=(100, 0))
        salario_mes_entry = Entry(self, textvariable=self.salario_mes_var, **estilo_entry, state="disabled")
        salario_mes_entry.grid(row=7, column=1, sticky="ew", ipady=6)

        Label(self, text="% IRPF", anchor="w", **estilo_label).grid(row=7, column=2, sticky="ew", padx=(50, 25))
        irpf_entry = Entry(self, textvariable=self.irpf_var, **estilo_entry, state="disabled")
        irpf_entry.grid(row=7, column=3, sticky="ew", ipady=6)

        Label(self, text="RETENCION IRPF", anchor="w", **estilo_label).grid(row=7, column=4, sticky="ew", padx=(50, 25))
        retencion_irpf_entry = Entry(self, textvariable=self.retencion_irpf_var, **estilo_entry, state="disabled")
        retencion_irpf_entry.grid(row=7, column=5, sticky="ew", padx=(0, 100), ipady=6)

        Label(self, text="PRORRATA PAGAS", anchor="w", **estilo_label).grid(row=8, column=0, sticky="ew", padx=(100, 0))
        prorrata_pagas_entry = Entry(self, textvariable=self.prorrata_pagas_var, **estilo_entry, state="disabled")
        prorrata_pagas_entry.grid(row=8, column=1, sticky="ew", ipady=6)

        Label(self, text="SEG. SOCIAL", anchor="w", **estilo_label).grid(row=8, column=2, sticky="ew", padx=(50, 25))
        seg_social_entry = Entry(self, textvariable=self.seg_social_var, **estilo_entry, state="disabled")
        seg_social_entry.grid(row=8, column=3, sticky="ew", ipady=6)

        Label(self, text="DEDUCCIÓN SS", anchor="w", **estilo_label).grid(row=8, column=4, sticky="ew", padx=(50, 25))
        deduccion_ss_entry = Entry(self, textvariable=self.deduccion_ss_var, **estilo_entry, state="disabled")
        deduccion_ss_entry.grid(row=8, column=5, sticky="ew", padx=(0, 100), ipady=10)

        msg_val = Label(self, text="MENSAJES VALIDACIÓN", font=("Helvetica", 18, "bold"), fg="red", bd=1, relief="solid")
        msg_val.grid(row=9, column=0, columnspan=4, sticky="ew", padx=(100, 0), ipady=10)

        Label(self, text="A PERCIBIR", anchor="w", **estilo_label).grid(row=9, column=4, sticky="ew", padx=(50, 25))
        a_percibir_entry = Entry(self, textvariable=self.a_percibir_var, state="disabled", bd=1, relief="solid", font=("Helvetica", 12), disabledbackground="#5ED3E8")
        a_percibir_entry.grid(row=9, column=5, sticky="ew", padx=(0, 100), ipady=10)

        
        
        Button(self, image=self.back_img, bd=0, command=lambda: controller.show_frame("View1")).place(x=10, y=10)
        
        def cargar_empleado():
            cod = codigo_entry.get()
            
            if cod == "" or not cod.isdigit() :
                msg_val.config(text="INTRODUZCA UN CÓDIGO VÁLIDO", fg="red")
                return
            
            if self.db_manager.usuario_existe(cod) and not self.db_manager.tiene_fecha_baja(cod):
                empleado = self.db_manager.get_empleado(cod)
                self.nombre_apellidos_var.set(empleado[1])
                self.fecha_inicio_var.set(empleado[2])
                self.fecha_nacimiento_var.set(empleado[3])
                self.direccion_var.set(empleado[5])
                self.nif_var.set(empleado[6])
                self.datos_bancarios_var.set(empleado[7])
                self.num_afiliacion_ss_var.set(empleado[8])
                self.numero_pagas_var.set(int(empleado[15]) + 12)
                self.salario_mes_var.set(empleado[14])
                self.irpf_var.set(empleado[16])                
                self.seg_social_var.set(empleado[17])
                
                
                self.salario_bruto_var.set("")
                self.prorrata_pagas_var.set("")
                self.deduccion_ss_var.set("")
                self.retencion_irpf_var.set("")
                self.a_percibir_var.set("")
                    
                msg_val.config(text="EMPLEADO CARGADO", fg="green")
            else:
                msg_val.config(text="EMPLEADO NO EXISTE", fg="red")
                self.salario_bruto_var.set("")
                self.prorrata_pagas_var.set("")
                self.deduccion_ss_var.set("")
                self.retencion_irpf_var.set("")
                self.a_percibir_var.set("")
                self.nombre_apellidos_var.set((""))
                self.fecha_inicio_var.set((""))
                self.fecha_nacimiento_var.set((""))
                self.direccion_var.set((""))
                self.nif_var.set((""))
                self.datos_bancarios_var.set((""))
                self.num_afiliacion_ss_var.set((""))
                self.numero_pagas_var.set((""))
                self.salario_mes_var.set((""))
                self.irpf_var.set((""))                
                self.seg_social_var.set((""))
                
                return
            
        Button(self, text="CARGAR EMPLEADO", **estilo_boton, command=cargar_empleado).grid(row=10, column=0, columnspan=2, padx=(100, 50))
        
        
        def calcular():
            #salario bruto | prorrata pagas | deducción ss | retención irpf | a percibir
            
            if nombre_apellidos_entry.get() == "" or not self.db_manager.usuario_existe(codigo_entry.get()):
                msg_val.config(text="CARGUE UN EMPLEADO VALIDO", fg="red")
                return
            
            salario_mensual = float(self.salario_mes_var.get())
            numero_pagas = int(self.numero_pagas_var.get())
            por_irpf = float(self.irpf_var.get())
            por_ss = float(self.seg_social_var.get())
            
            salario_bruto = salario_mensual * numero_pagas
            prorrata_pagas = salario_bruto / 12
            
            deduccion_ss = (salario_mensual * por_ss) / 100
            retencion_irpf = (salario_mensual * por_irpf) / 100
            
            a_percibir = salario_mensual - deduccion_ss - retencion_irpf
            
            self.salario_bruto_var.set(salario_bruto)
            self.prorrata_pagas_var.set(prorrata_pagas)
            self.deduccion_ss_var.set(deduccion_ss)
            self.retencion_irpf_var.set(retencion_irpf)
            self.a_percibir_var.set(a_percibir)
            
            msg_val.config(text="CÁLCULO REALIZADO", fg="green")
            
        Button(self, text="CALCULAR", **estilo_boton, command=calcular).grid(row=10, column=2, columnspan=2, padx=(50, 50))
        
        def generarPdf():
            if nombre_apellidos_entry.get() == "" or not self.db_manager.usuario_existe(codigo_entry.get()) or self.db_manager.tiene_fecha_baja(codigo_entry.get()):
                msg_val.config(text="CARGUE UN EMPLEADO VALIDO", fg="red")
                return
            elif self.salario_bruto_var.get() == "":
                msg_val.config(text="CALCULE LOS DATOS ANTES DE GUARDAR", fg="red")
                return
            
            self.pdf.generar_pdf(
            self.nombre_apellidos_var.get(), 
            self.direccion_var.get(), 
            self.nif_var.get(),
            self.datos_bancarios_var.get(),
            self.num_afiliacion_ss_var.get(),
            self.salario_bruto_var.get(),
            self.salario_mes_var.get(),
            self.a_percibir_var.get(),
            self.numero_pagas_var.get(),
            self.irpf_var.get(),
            self.seg_social_var.get(),
            self.retencion_irpf_var.get(),
            self.deduccion_ss_var.get()
            )
            
            msg_val.config(text="NOMINA GUARDADA", fg="green")
        
        Button(self, text="GUARDAR PDF", **estilo_boton, command=generarPdf).grid(row=10, column=4, columnspan=2, padx=(0, 100))
import tkinter as tk
from tkinter import Label, Button,PhotoImage, Entry

class View5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

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
        
        Label(self, text="CÓDIGO", **estilo_label).grid(row=0, column=0, columnspan=1, padx=(100, 0))
        Entry(self, **estilo_entry).grid(row=1, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="NOMBRE Y APELLIDOS", **estilo_label).grid(row=0, column=1, columnspan=5)
        Entry(self, **estilo_entry,state="disabled").grid(row=1, column=1, columnspan=5, sticky="ew", padx=(25,100), ipady=6)

        
        Label(self, text="FECHA INICIO", **estilo_label).grid(row=2, column=0, columnspan=1,padx=(100,25))
        Entry(self, **estilo_entry,state="disabled").grid(row=3, column=0, columnspan=1, sticky="ew",padx=(100,25), ipady=6)
        
        Label(self, text="FECHA NACIMIENTO", **estilo_label).grid(row=2, column=1, columnspan=1, padx=(25,25) )
        Entry(self, **estilo_entry,state="disabled").grid(row=3, column=1, columnspan=1, sticky="ew",padx=(25,25), ipady=6)
        
        Label(self, text="DIRECCIÓN", **estilo_label).grid(row=2, column=2, columnspan=4, padx=(25, 100))
        Entry(self, **estilo_entry,state="disabled").grid(row=3, column=2, columnspan=4, sticky="ew", padx=(25, 100), ipady=6)


        
        
        Label(self, text="NIF", **estilo_label).grid(row=4, column=0, columnspan=1, padx=(100, 25), sticky="ew")
        Entry(self, **estilo_entry,state="disabled").grid(row=5, column=0, columnspan=1, sticky="ew", padx=(100, 25), ipady=6)

        Label(self, text="DATOS BANCARIOS", **estilo_label).grid(row=4, column=1, columnspan=3, padx=(25, 25), sticky="ew")
        Entry(self, **estilo_entry,state="disabled").grid(row=5, column=1, columnspan=3, sticky="ew", padx=(25, 25), ipady=6)

        Label(self, text="NUMERO DE AFILIACIÓN SS", **estilo_label).grid(row=4, column=4, columnspan=2, padx=(25, 100), sticky="ew")
        Entry(self, **estilo_entry,state="disabled").grid(row=5, column=4, columnspan=2, sticky="ew", padx=(25, 100), ipady=6)
        
        


        Label(self, text="SALARIO BRUTO", anchor="w", **estilo_label).grid(row=6, column=0, sticky="ew", padx=(100,0))
        Entry(self, **estilo_entry,state="disabled").grid(row=6, column=1, sticky="ew", ipady=6)

        Label(self, text="NUMERO PAGAS", anchor="w", **estilo_label).grid(row=6, column=2, sticky="ew", padx=(50,25))
        Entry(self, **estilo_entry,state="disabled").grid(row=6, column=3, sticky="ew", ipady=6)



        

        Label(self, text="SALARIO MES", anchor="w", **estilo_label).grid(row=7, column=0, sticky="ew", padx=(100,0))
        Entry(self, **estilo_entry,state="disabled").grid(row=7, column=1, sticky="ew", ipady=6)

        Label(self, text="% IRPF", anchor="w", **estilo_label).grid(row=7, column=2, sticky="ew", padx=(50,25))
        Entry(self, **estilo_entry,state="disabled").grid(row=7, column=3, sticky="ew", ipady=6)

        Label(self, text="RETENCION IRPF", anchor="w", **estilo_label).grid(row=7, column=4, sticky="ew", padx=(50,25))
        Entry(self, **estilo_entry).grid(row=7, column=5, sticky="ew", padx=(0,100), ipady=6)

        Label(self, text="PRORRATA PAGAS", anchor="w", **estilo_label).grid(row=8, column=0, sticky="ew", padx=(100,0))
        Entry(self, **estilo_entry,state="disabled").grid(row=8, column=1, sticky="ew", ipady=6)

        Label(self, text="SEG. SOCIAL", anchor="w", **estilo_label).grid(row=8, column=2, sticky="ew", padx=(50,25))
        Entry(self, **estilo_entry,state="disabled").grid(row=8, column=3, sticky="ew", ipady=6)

        Label(self, text="DEDUCCIÓN SS", anchor="w", **estilo_label).grid(row=8, column=4, sticky="ew", padx=(50,25))
        Entry(self, **estilo_entry).grid(row=8, column=5, sticky="ew", padx=(0,100), ipady=10)

        Label(self, text="MENSAJES VALIDACIÓN", font=("Helvetica",18,"bold"), fg="red", bd=1, relief="solid").grid(row=9, column=0, columnspan=4, sticky="ew",padx=(100,0), ipady=10)

        Label(self, text="A PERCIBIR", anchor="w", **estilo_label).grid(row=9, column=4, sticky="ew", padx=(50,25))
        Entry(self, state="disabled", bd=1, relief="solid",font=("Helvetica",12),disabledbackground="#5ED3E8",).grid(row=9, column=5, sticky="ew", padx=(0,100), ipady=10)

        Button(self, text="INSERTAR", **estilo_boton).grid(row=10, column=4,columnspan=2, padx=(0,100))
        Button(self, text="CALCULAR", **estilo_boton).grid(row=10, column=2,columnspan=2, padx=(50,50))
        Button(self, text="CARGAR EMPLEADO", **estilo_boton).grid(row=10, column=0,columnspan=2, padx=(100,50))
        Button(self, image=self.back_img,bd=0, command=lambda: controller.show_frame("View1")).place(x=10, y=10)
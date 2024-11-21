import tkinter as tk
from tkinter import Label, Button, PhotoImage, Entry

class View3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.back_img = PhotoImage(file="back.png").subsample(10)
       
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
            "font": ("Helvetica", 20, "bold")
        }

        estilo_entry = {
            "font": ("Helvetica", 12)
           
        }

        # Configuración filas y columnas
        num_filas = 4
        num_columnas = 2
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)
        ############################################
        

        Label(self, text="CÓDIGO EMPLEADO", **estilo_label).grid(row=0, column=0, pady=(200,0))
        Entry(self, **estilo_entry).grid(row=1, column=0, ipady=6, sticky="ew", padx=(150,150), pady=(0,100))

        Label(self, text="FECHA DE ABAJA", **estilo_label).grid(row=0, column=1, pady=(200,0))
        Entry(self, **estilo_entry).grid(row=1, column=1, ipady=6, sticky="ew", padx=(150,150), pady=(0,100))

        

        Label(self, text="MENSAJES VALIDACIÓN", fg="red", font=("Helvetica",16)).grid(row=2, column=0, columnspan=2)

        Button(self, text="CONFIRMAR", **estilo_boton).grid(row=4, column=0, columnspan=2, pady=(0,100))

        Button(self, image=self.back_img,bd=0, command=lambda: controller.show_frame("View1")).place(x=10, y=10)
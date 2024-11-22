import tkinter as tk
from tkinter import PhotoImage, Label, Button

class View1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
       

        # Mantén una referencia al objeto PhotoImage
        self.logo = PhotoImage(file="assets\logo.png").subsample(2)

        # #E87288 rosa
        # #FFE781 amarillo
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

        titulo = {
            "font": ("Helvetica", 30, "bold", "italic"), 
            "fg": "black",
        }

        # Definir el número de filas y columnas
        num_filas = 4
        num_columnas = 4

        # Configurar las filas y columnas
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)

        Label(self, text="Nominator", **titulo).grid(row=0, column=0, columnspan=4)
        Label(self, image=self.logo).grid(row=1, column=1, columnspan=2)

        Button(self, text="Altas", **estilo_boton, command=lambda: controller.show_frame("View2")).grid(row=2, column=1)
        Button(self, text="Informes", **estilo_boton, command=lambda: controller.show_frame("View4")).grid(row=3, column=1)

        Button(self, text="Bajas", **estilo_boton, command=lambda: controller.show_frame("View3")).grid(row=2, column=2)
        Button(self, text="Nóminas", **estilo_boton, command=lambda: controller.show_frame("View5")).grid(row=3, column=2)
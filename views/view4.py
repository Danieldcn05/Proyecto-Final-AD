import tkinter as tk
from tkinter import Label, Button, PhotoImage
from empleado_manager import EmpleadoManager

class View4(tk.Frame):
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

        # Configuración filas y columnas
        num_filas = 6
        num_columnas = 4
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)
        ############################################

        Label(self, text="EMPLEADOS ALTA", font=("Helvetica", 20, "bold"), fg="black").grid(row=0, column=0)
        Label(self, text="25", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=1, column=0)

        Label(self, text="% MUJERES", font=("Helvetica", 20), fg="black").grid(row=2, column=0)
        Label(self, text="10", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=3, column=0)

        Label(self, text="% HOMBRES", font=("Helvetica", 20), fg="black").grid(row=4, column=0)
        Label(self, text="15", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=5, column=0)



        Label(self, text="EMPLEADOS BAJA", font=("Helvetica", 20, "bold"), fg="black").grid(row=0, column=1)
        Label(self, text="25", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=1, column=1)

        Label(self, text="% MUJERES", font=("Helvetica", 20), fg="black").grid(row=2, column=1)
        Label(self, text="10", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=3, column=1)

        Label(self, text="% HOMBRES", font=("Helvetica", 20), fg="black").grid(row=4, column=1)
        Label(self, text="15", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=5, column=1)



        Label(self, text="MEDIA EDADES", font=("Helvetica", 20, "bold"), fg="black").grid(row=0, column=2)
        Label(self, text="25", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=1, column=2)

        Label(self, text="MUJERES", font=("Helvetica", 20), fg="black").grid(row=2, column=2)
        Label(self, text="10", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=3, column=2)

        Label(self, text="HOMBRES", font=("Helvetica", 20), fg="black").grid(row=4, column=2)
        Label(self, text="15", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=5, column=2)



        Label(self, text="RETRIBUCIÓN MEDIA", font=("Helvetica", 20, "bold"), fg="black").grid(row=0, column=3)
        Label(self, text="25", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=1, column=3)

        Label(self, text="MUJERES", font=("Helvetica", 20), fg="black").grid(row=2, column=3)
        Label(self, text="10", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=3, column=3)

        Label(self, text="HOMBRES", font=("Helvetica", 20), fg="black").grid(row=4, column=3)
        Label(self, text="15", font=("Helvetica", 20, "bold"), fg="black", bd=1, relief="solid").grid(row=5, column=3)
        
        Button(self, image=self.back_img,bd=0, command=lambda: controller.show_frame("View1")).place(x=10, y=10)
        
        
      
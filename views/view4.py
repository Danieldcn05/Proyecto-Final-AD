import tkinter as tk
from tkinter import Label, Button, PhotoImage
from empleado_manager import EmpleadoManager
import matplotlib.pyplot as plt
from bd.db_setup import DatabaseManager

class View4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db_manager = DatabaseManager()
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
        num_filas = 1
        num_columnas = 4
        for i in range(num_filas):
            self.grid_rowconfigure(i, weight=1)

        for j in range(num_columnas):
            self.grid_columnconfigure(j, weight=1)
        ############################################
        
      
        

        

        
        Button(self, image=self.back_img,bd=0, command=lambda: controller.show_frame("View1")).place(x=10, y=10)
        
        def generar_grafico_alta():
            
            empleados_totales = self.db_manager.get_total_empleados()
            hombres_totales = self.db_manager.get_total_hombres()
            mujeres_totales = abs(empleados_totales - hombres_totales)
            # Datos
            labels = ['Hombres', 'Mujeres']
            sizes = [hombres_totales, mujeres_totales]
            colors = ['lightskyblue', 'lightcoral']

            
            # Crear el gráfico de torta
            fig, ax = plt.subplots()
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

            # Añadir título
            plt.title('Empleados dados de alta')

            # Calcular el total
            total = sum(sizes)

            # Añadir anotación con el total
            plt.annotate(f'Total: {total}', xy=(0, 0), xytext=(0, -1.4), ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

            # Mostrar el gráfico
            plt.show()
            
        # Botón EMPLEADOS ALTA
        alta_btn = Button(self, text="Empleados Alta",**estilo_boton, command=generar_grafico_alta)
        alta_btn.grid(row=0, column=0, padx=10, pady=10)
        
        def generar_grafico_baja():
            
            empleados_totales = self.db_manager.get_total_bajas()
            hombres_totales = self.db_manager.get_total_hom_bajas()
            mujeres_totales = abs(empleados_totales - hombres_totales)
            # Datos
            labels = ['Hombres', 'Mujeres']
            sizes = [hombres_totales, mujeres_totales]
            colors = ['lightskyblue', 'lightcoral']

            
            # Crear el gráfico de torta
            fig, ax = plt.subplots()
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

            # Añadir título
            plt.title('Empleados dados de baja')

            # Calcular el total
            total = sum(sizes)

            # Añadir anotación con el total
            plt.annotate(f'Total: {total}', xy=(0, 0), xytext=(0, -1.4), ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

            # Mostrar el gráfico
            plt.show()
          # Botón EMPLEADOS BAJA
        baja_btn = Button(self, text="Empleados Baja",**estilo_boton, command=generar_grafico_baja)
        baja_btn.grid(row=0, column=1, padx=10, pady=10)
        
        
        
        
        def generar_grafica_edades():
            media_edad_hombres, media_edad_mujeres = self.db_manager.get_media_edad()
        
            # Nombres de las categorías
            categorias = ['Hombres', 'Mujeres']
            # Valores de las medias de edad
            valores = [media_edad_hombres, media_edad_mujeres]
        
            # Crear el gráfico de barras
            fig, ax = plt.subplots()
            ax.bar(categorias, valores, color=['lightskyblue', 'lightcoral'])
        
            # Añadir título y etiquetas
            ax.set_title('Comparación de la Media de Edad')
            ax.set_ylabel('Media de Edad')
            ax.set_xlabel('Género')
        
            # Establecer un límite máximo fijo en el eje y
            ax.set_ylim(0, 65)
        
            # Añadir etiquetas de valor encima de las barras
            for i, v in enumerate(valores):
                ax.text(i, v + 0.5, f'{int(v)}', ha='center', va='bottom')
        
            # Mostrar el gráfico
            plt.show()
        
        media_edades_btn = Button(self, text="Media Edades",**estilo_boton, command=generar_grafica_edades)
        media_edades_btn.grid(row=0, column=2, padx=10, pady=10)
        
        
        
        def generar_grafica_retribución():
            media_salario_hombres, media_salario_mujeres = self.db_manager.get_media_salario()
        
            # Nombres de las categorías
            categorias = ['Hombres', 'Mujeres']
            # Valores de las medias de salario
            valores = [media_salario_hombres, media_salario_mujeres]
        
            # Crear el gráfico de barras
            fig, ax = plt.subplots()
            ax.bar(categorias, valores, color=['lightskyblue', 'lightcoral'])
        
            # Añadir título y etiquetas
            ax.set_title('Comparación de la Media de Salario')
            ax.set_ylabel('Media de Salario')
            ax.set_xlabel('Género')
        
            # Establecer un límite máximo fijo en el eje y
            ax.set_ylim(0, 5000)
        
            # Añadir etiquetas de valor encima de las barras
            for i, v in enumerate(valores):
                ax.text(i, v + 50, f'{int(v)}', ha='center', va='bottom')
        
            # Mostrar el gráfico
            plt.show()
            
        
        # Botón RETRIBUCIÓN MEDIA
        retribucion_media_btn = Button(self, text="Retribución Media",**estilo_boton, command=generar_grafica_retribución)
        retribucion_media_btn.grid(row=0, column=3, padx=10, pady=10)
import matplotlib.pyplot as plt

# Datos
labels = ['G1', 'G2', 'G3', 'G4']
men_means = [20, 35, 30, 35]
women_means = [25, 32, 34, 20]

# Crear el gráfico de barras apiladas
width = 0.35  # el ancho de las barras
fig, ax = plt.subplots()
ax.bar(labels, men_means, width, label='Hombres')
ax.bar(labels, women_means, width, bottom=men_means, label='Mujeres')

# Añadir título y etiquetas
ax.set_title('Gráfico de Barras Apiladas')
ax.set_xlabel('Grupos')
ax.set_ylabel('Valores')
ax.legend()

# Mostrar el gráfico
plt.show()
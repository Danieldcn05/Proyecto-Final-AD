import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 6, 8, 10]
y2 = [2, 2, 7, 10, 12]

# Crear el gráfico de área
plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4)

# Añadir título y etiquetas
plt.title('Gráfico de Área')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()
import matplotlib.pyplot as plt

# Datos
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # resaltar el primer segmento

# Crear el gráfico de torta
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Añadir título
plt.title('Gráfico de Torta')

# Mostrar el gráfico
plt.show()
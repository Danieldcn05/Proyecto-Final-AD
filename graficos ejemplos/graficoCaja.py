import matplotlib.pyplot as plt
import numpy as np

# Datos
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Crear el gráfico de caja
plt.boxplot(data, vert=True, patch_artist=True)

# Añadir título y etiquetas
plt.title('Gráfico de Caja')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()
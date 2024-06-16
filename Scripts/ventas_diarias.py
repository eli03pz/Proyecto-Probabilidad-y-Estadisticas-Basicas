
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de ventas de tazas de café (sin "nd")
ventas = [61, 46, 57, 40, 33, 56, 47, 58, 42, 46, 63, 47, 55, 38, 35, 53, 45, 59, 38, 57, 68, 72, 60, 42, 50, 71, 66, 72, 38, 60, 74, 45, 64, 32, 56, 39, 37, 27, 35, 56, 9, 63, 30, 42, 69, 52, 56]

# Calcular estadísticas descriptivas
media = np.mean(ventas)
mediana = np.median(ventas)
moda = np.bincount(ventas).argmax()
rango = np.ptp(ventas)
varianza = np.var(ventas)
desviacion_estandar = np.std(ventas)

# Crear visualizaciones
plt.figure(figsize=(14, 6))

# Histograma
plt.subplot(1, 2, 1)
sns.histplot(ventas, kde=True, bins=10)
plt.title('Ventas diarias de tazas de café')
plt.xlabel('Número de tazas vendidas')
plt.ylabel('Frecuencia')

# Gráfico de caja
plt.subplot(1, 2, 2)
sns.boxplot(x=ventas)
plt.title('Ventas diarias de tazas de café')
plt.xlabel('Número de tazas vendidas')

# Mostrar gráficos
plt.tight_layout()
plt.show()

(media, mediana, moda, rango, varianza, desviacion_estandar)

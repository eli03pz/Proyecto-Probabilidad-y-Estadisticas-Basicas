import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de temperatura máxima diaria en Fahrenheit
temperaturas = [
    36, 34, 39, 40, 36, 26, 34, 33, 20, 37,
    38, 33, 39, 35, 31, 29, 26, 28, 30, 26,
    29, 29, 34, 39, 36, 33, 28, 33, 35, 40,
    39, 39, 45, 47, 48, 61, 64, 64, 65, 47,
    62, 66, 56, 49, 56, 62, 76, 80
]

# Calcular estadísticas descriptivas
media_temp = np.mean(temperaturas)
mediana_temp = np.median(temperaturas)
moda_temp = np.bincount(temperaturas).argmax()
rango_temp = np.ptp(temperaturas)
varianza_temp = np.var(temperaturas)
desviacion_estandar_temp = np.std(temperaturas)

# Crear visualizaciones
plt.figure(figsize=(14, 6))

# Histograma
plt.subplot(1, 2, 1)
sns.histplot(temperaturas, kde=True, bins=10, color = 'orange')
plt.title('Temperaturas máximas diarias')
plt.xlabel('Temperatura máxima [°F]')
plt.ylabel('Frecuencia')

# Gráfico de caja
plt.subplot(1, 2, 2)
sns.boxplot(x=temperaturas, color='orange')
plt.title('Temperaturas máximas diarias')
plt.xlabel('Temperatura máxima [°F]')

# Mostrar gráficos
plt.tight_layout()
plt.show()

(media_temp, mediana_temp, moda_temp, rango_temp, varianza_temp, desviacion_estandar_temp)
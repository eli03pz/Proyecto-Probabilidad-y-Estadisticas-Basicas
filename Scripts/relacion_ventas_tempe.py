import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Datos proporcionados
data = {
    'Sales': [
        199.95, 195.74, 102.68, 162.88, 101.76, 186.94, 120.18, 228.78, 88.02, 119.57,
        172.31, 137.65, 197.56, 70, 97, 181.43, 125.57, 180.63, 75.87, 150.51,
        177.41, 153.84, 205.36, 118.54, 138.04, 236.01, 149.58, 206.17, 93.1, 151.91,
        217.29, 148.24, 168.08, None, 130.77, 164.54, 121.41, 127.93, 61.94, 128.59,
        159.23, 148.08, 164.86, 74.13, 82.96, 240.87, 151.52, 150.99
    ],
    'Max Daily Temperature (F)': [
        36, 34, 39, 40, 36, 26, 34, 33, 20, 37, 38, 33, 39, 35, 31, 29, 26, 28, 30, 26,
        29, 29, 34, 39, 36, 33, 28, 33, 35, 40, 39, 39, 45, 47, 48, 61, 64, 64, 65, 47,
        62, 66, 56, 49, 56, 62, 76, 80
    ]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Eliminar filas con valores faltantes
df_clean = df.dropna()

# Calcular el coeficiente de correlación de Pearson
correlation, p_value = pearsonr(df_clean['Sales'], df_clean['Max Daily Temperature (F)'])

# Crear un diagrama de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Max Daily Temperature (F)', y='Sales', data=df_clean)
sns.regplot(x='Max Daily Temperature (F)', y='Sales', data=df_clean, scatter=False, color='green')
plt.title('Relación entre las Ventas y la Temperatura Máxima Diaria')
plt.xlabel('Temperatura Máxima Diaria [°F]')
plt.ylabel('Ventas')
plt.show()

correlation, p_value
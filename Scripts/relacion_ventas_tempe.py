import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
# Asegurarse de que el script pueda encontrar el módulo Data.datos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.datos import data


# Convertir a DataFrame
df = pd.DataFrame(data)

# Eliminar filas con valores faltantes
df_clean = df.dropna()

# Calcular el coeficiente de correlación de Pearson
correlation, p_value = pearsonr(df_clean['Ventas totales'], df_clean['Temperaturas Max Diaria'])

# Crear un diagrama de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperaturas Max Diaria', y='Ventas totales', data=df_clean)
sns.regplot(x='Temperaturas Max Diaria', y='Ventas totales', data=df_clean, scatter=False, color='green')
plt.title('Relación entre las Ventas y la Temperatura Máxima Diaria')
plt.xlabel('Temperatura Máxima Diaria [°F]')
plt.ylabel('Ventas')
plt.show()

correlation, p_value
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

# Asegurarse de que el script pueda encontrar el módulo Data.datos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data.datos import data

# Crear DataFrame
df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
df = df.dropna()  # Eliminar filas con valores NaN
df = df.sort_values('Fecha')

# Colores para las barras
colors = ["#241811"] * len(df)  # Inicializar todos los colores de barras

# Encontrar la fecha con la mayor cantidad de artículos desperdiciados
max_value_index = df['Total de articulos desperdiciados'].idxmax()
max_value_date = df.loc[max_value_index, 'Fecha']
max_value = df.loc[max_value_index, 'Total de articulos desperdiciados']
colors[max_value_index] = "#D4A979"  # Cambiar color de la barra con el valor máximo

# Crear gráfico de barras con etiquetas de fechas en el eje x
plt.figure(figsize=(14, 8))
bars = plt.bar(df['Fecha'], df['Total de articulos desperdiciados'], color=colors)
plt.xlabel('Fecha')
plt.ylabel('Total de artículos desperdiciados')
plt.title('Artículos desperdiciados por fecha')

# Etiquetar solo la barra con la mayor cantidad de artículos desperdiciados
for bar in bars:
    height = bar.get_height()
    if height == max_value:
        plt.text(bar.get_x() + bar.get_width() / 2, height, 
                 f'{max_value_date.strftime("%d/%m/%Y")}\n{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Ajustar las etiquetas del eje x
plt.xticks(rotation=360)

# Quitar las líneas de cuadrícula
plt.grid(False)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
# Asegurarse de que el script pueda encontrar el módulo Data.datos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.datos import data

# Datos de ventas

# Crear DataFrame
sales_df = pd.DataFrame(data)
sales_df['Fecha'] = pd.to_datetime(sales_df['Fecha'], format='%d/%m/%Y')
sales_df = sales_df.dropna()  # Eliminar filas con valores NaN
sales_df = sales_df.sort_values('Ventas totales', ascending=False)

# Colores para las barras
colors = ["#241811", "#D4A979", "#E3C88F", "#C2C995", "#A8BD95"]

# Crear gráfico de barras para las ventas totales
plt.figure(figsize=(14, 8))
plt.bar(sales_df['Fecha'], sales_df['Ventas totales'], color=colors)
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por Fecha')
plt.xticks(sales_df['Fecha'], sales_df['Fecha'].dt.strftime('%d/%m/%Y'), rotation=90)
plt.grid(axis='y')

plt.show()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
from Data.datos import data


# Crear el DataFrame
df = pd.DataFrame(data)

# Reemplazar 'na' con NaN para permitir cálculos
df.replace('na', pd.NA, inplace=True)

# Convertir las columnas numéricas a tipo float
for col in df.columns[3:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Ventas de productos por día
ventas_por_dia = df.groupby('Día de la semana')[['Sándwiches de Pan Vendidos', 'Envolturas Vendidas', 'Muffins Vendidos']].sum()
ventas_por_dia.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas de Productos por Día de la Semana')
plt.ylabel('Cantidad Vendida')
plt.xlabel('Día de la Semana')
plt.show()

# Venta de productos por tipo de producto
ventas_por_producto = df[['Sándwiches de Pan Vendidos', 'Envolturas Vendidas', 'Muffins Vendidos']].sum()
ventas_por_producto.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por Tipo de Producto')
plt.ylabel('Cantidad Vendida')
plt.xlabel('Producto')
plt.show()

# Ventas totales por mes
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
df['Mes'] = df['Fecha'].dt.month
ventas_por_mes = df.groupby('Mes')[['Sándwiches de Pan Vendidos', 'Envolturas Vendidas', 'Muffins Vendidos']].sum()
ventas_por_mes.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas Totales por Mes')
plt.ylabel('Cantidad Vendida')
plt.xlabel('Mes')
plt.show()

# Desperdicio de productos por tipo de producto
desperdicio_por_producto = df[['Desperdicios de Sándwiches de Pan', 'Desechos de Envolturas', 'Muffins Desperdiciados']].sum()
desperdicio_por_producto.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Desperdicio por Tipo de Producto')
plt.ylabel('')
plt.show()

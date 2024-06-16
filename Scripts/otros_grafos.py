import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
from Data.datos import data
import mplcursors

# Crear el DataFrame
df = pd.DataFrame(data)

# Reemplazar 'na' con NaN para permitir cálculos
df.replace('na', pd.NA, inplace=True)

# Convertir las columnas numéricas a tipo float
for col in df.columns[3:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
# Colores personalizados
colores = ['#A69A81', '#E0D3B8', '#EB9E6E', '#EB6E6E', '#706F6B', '#8C8C8C', '#B2B2B2', '#D9D9D9', '#F0F0F0', '#241811','#D4A979','#E3C88F','#C2C995','#A8BD95']

# Nombres personalizados para las etiquetas de los productos
nombres_productos = ['Sándwiches', 'Envolturas', 'Muffins', 'Galletas', 'Vasos Frutas', 'Papitas', 'Jugos', 'Refrescos', 'Cafés']

# Ventas de productos por días
ventas_por_dia = df.groupby('Día de la semana')[['Sándwiches de Pan Vendidos', 'Envolturas Vendidas', 'Muffins Vendidos', 'Galletas Vendidas', 'Vasos de Frutas Vendidos', 'Papitas Fritas Vendidas', 'Jugos Vendidos', 'Refrescos Vendidos', 'Cafes Vendidos']].sum()
ax = ventas_por_dia.plot(kind='bar', figsize=(10, 6), color=colores[:ventas_por_dia.shape[1]])
plt.title('Ventas de Productos por Día de la Semana')
plt.ylabel('Cantidad Vendida')
plt.xlabel('Día de la Semana')

# Agregar cursores interactivos
cursor = mplcursors.cursor(ax, hover=True)
@cursor.connect("add")
def on_add(sel):
    sel.annotation.set(text=f'{sel.target[1]:.0f}', ha='center', fontsize=8, backgroundcolor='white')

plt.show()

# Venta de productos por tipo de producto
ventas_por_producto = df[['Sándwiches de Pan Vendidos', 'Envolturas Vendidas', 'Muffins Vendidos', 'Galletas Vendidas',
                                                 'Vasos de Frutas Vendidos', 'Papitas Fritas Vendidas', 'Jugos Vendidos', 'Refrescos Vendidos', 'Cafes Vendidos']].sum()
ax = ventas_por_producto.plot(kind='bar', figsize=(10, 6), color = colores)
plt.title('Ventas por Tipo de Producto')
plt.ylabel('Cantidad Vendida')
plt.xlabel('Producto')
plt.xticks( ticks=range(len(nombres_productos)), labels=nombres_productos , rotation = 360)

# Agregar cursores interactivos
cursor = mplcursors.cursor(ax, hover=True)
@cursor.connect("add")
def on_add(sel):
    sel.annotation.set(text=f'{sel.target[1]:.0f}', ha='center', fontsize=8, backgroundcolor='white')

plt.show()


# Ventas totales por mes
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
df['Mes'] = df['Fecha'].dt.month
ventas_por_mes = df.groupby('Mes')[['Sándwiches de Pan Vendidos', 'Envolturas Vendidas', 'Muffins Vendidos']].sum()
ventas_por_mes.plot(kind='bar', figsize=(10, 6), color= colores)
plt.title('Ventas Totales por Mes')
plt.ylabel('Cantidad Vendida')
plt.xlabel('Mes')
plt.show()

# Desperdicio de productos por tipo de producto
desperdicio_por_producto = df[['Desperdicios de Sándwiches de Pan', 'Desechos de Envolturas', 'Muffins Desperdiciados', 'Galletas Desechadas',
                                                 'Desechos de Vasos de Frutas']].sum()
desperdicio_por_producto.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), color = colores)
plt.title('Desperdicio por Tipo de Producto')
plt.ylabel('')
plt.show()

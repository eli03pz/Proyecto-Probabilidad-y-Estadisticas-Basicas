import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

# Asegúrate de que el script pueda encontrar el módulo Data.datos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data.datos import data

# Crear DataFrame
df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

# Gráfico de dispersión de los datos originales
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperaturas Max Diaria'], df['Ventas totales'], color='blue')
plt.xlabel('Temperatura Máxima Diaria (°C)')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales vs Temperatura Máxima Diaria')
plt.grid(True)
plt.show()

# Realizar la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df['Temperaturas Max Diaria'], df['Ventas totales'])

# Imprimir los resultados de la regresión
print(f"Pendiente: {slope}")
print(f"Intersección: {intercept}")
print(f"Coeficiente de correlación: {r_value}")
print(f"Valor p: {p_value}")
print(f"Error estándar: {std_err}")

# Gráfico de dispersión con la línea de regresión
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperaturas Max Diaria'], df['Ventas totales'], color='blue', label='Datos Originales')
plt.plot(df['Temperaturas Max Diaria'], intercept + slope * df['Temperaturas Max Diaria'], 'r', label='Línea de Regresión')
plt.xlabel('Temperatura Máxima Diaria (°C)')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales vs Temperatura Máxima Diaria con Regresión Lineal')
plt.legend()
plt.grid(True)
plt.show()

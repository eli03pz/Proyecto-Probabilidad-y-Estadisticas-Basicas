import matplotlib.pyplot as plt
import pandas as pd

# Datos de ventas
sales_data = {
    "Fecha": ["19/1/2010", "20/1/2010", "21/1/2010", "22/1/2010", "25/1/2010", "26/1/2010", "27/1/2010", "28/1/2010", 
            "29/1/2010", "1/2/2010", "2/2/2010", "3/2/2010", "4/2/2010", "5/2/2010", "8/2/2010", "9/2/2010", 
            "10/2/2010", "11/2/2010", "12/2/2010", "15/2/2010", "16/2/2010", "17/2/2010", "18/2/2010", "19/2/2010",
            "22/2/2010", "23/2/2010", "24/2/2010", "25/2/2010", "26/2/2010", "1/3/2010", "2/3/2010", "3/3/2010", 
            "4/3/2010", "5/3/2010", "15/3/2010", "16/3/2010", "17/3/2010", "18/3/2010", "19/3/2010", "22/3/2010",
            "23/3/2010", "24/3/2010", "25/3/2010", "26/3/2010", "29/3/2010", "30/3/2010", "31/3/2010", "1/4/2010"],
    "Día de la semana": ["Martes", "Miércoles", "Jueves", "Viernes", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
                        "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Lunes", "Martes", "Miércoles", "Jueves",
                        "Viernes", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Lunes", "Martes", "Miércoles",
                        "Jueves", "Viernes", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Lunes", "Martes",
                        "Miércoles", "Jueves", "Viernes", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Lunes",
                        "Martes", "Miércoles", "Jueves"],
    "Ventas Totales": [199.95, 195.74, 102.68, 162.88, 101.76, 186.94, 120.18, 228.78, 88.02, 119.57, 172.31, 137.65, 197.56,
                    70, 97, 181.43, 125.57, 180.63, 75.87, 150.51, 177.41, 153.84, 205.36, 118.54, 138.04, 236.01, 
                    149.58, 206.17, 93.1, 151.91, 217.29, 148.24, 168.08, float('nan'), 130.77, 164.54, 121.41, 127.93, 
                    61.94, 128.59, 159.23, 148.08, 164.86, 74.13, 82.96, 240.87, 151.52, 150.99]
}

# Crear DataFrame
sales_df = pd.DataFrame(sales_data)
sales_df['Fecha'] = pd.to_datetime(sales_df['Fecha'], format='%d/%m/%Y')
sales_df = sales_df.dropna()  # Eliminar filas con valores NaN
sales_df = sales_df.sort_values('Ventas Totales', ascending=False)

# Colores para las barras
colors = ["#241811", "#D4A979", "#E3C88F", "#C2C995", "#A8BD95"]

# Crear gráfico de barras para las ventas totales
plt.figure(figsize=(14, 8))
plt.bar(sales_df['Fecha'], sales_df['Ventas Totales'], color=colors)
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por Fecha')
plt.xticks(sales_df['Fecha'], sales_df['Fecha'].dt.strftime('%d/%m/%Y'), rotation=90)
plt.grid(axis='y')

plt.show()

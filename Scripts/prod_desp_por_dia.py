import matplotlib.pyplot as plt
import pandas as pd

# Datos
data = {
    "Fecha": ["19/1/2010", "20/1/2010", "21/1/2010", "22/1/2010", "25/1/2010", "26/1/2010", "27/1/2010", "28/1/2010",
            "29/1/2010", "1/2/2010", "2/2/2010", "3/2/2010", "4/2/2010", "5/2/2010", "8/2/2010", "9/2/2010", 
            "10/2/2010", "11/2/2010", "12/2/2010", "15/2/2010", "16/2/2010", "17/2/2010", "18/2/2010", "19/2/2010",
            "22/2/2010", "23/2/2010", "24/2/2010", "25/2/2010", "26/2/2010", "1/3/2010", "2/3/2010", "3/3/2010", 
            "4/3/2010", "5/3/2010", "15/3/2010", "16/3/2010", "17/3/2010", "18/3/2010", "19/3/2010", "22/3/2010",
            "23/3/2010", "24/3/2010", "25/3/2010", "26/3/2010", "29/3/2010", "30/3/2010", "31/3/2010", "1/4/2010"],
    "Total de artículos desperdiciados": [16, 39, 5, 10, 0, 4, 9, 1, 20, 9, 9, 6, 1, 4, 7, 1, 3, 0, 0, 5, 1, 2, 2, 2, 0, 0,
                                        1, 4, 2, 4, 2, 4, 0, float('nan'), 0, 3, 7, 10, 12, 10, 9, 4, 2, 5, 7, 1, 4, 0]
}

# Crear DataFrame
df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
df = df.dropna()  # Eliminar filas con valores NaN
df = df.sort_values('Fecha')

# Colores para las barras
colors = ["#241811", "#D4A979", "#E3C88F", "#C2C995", "#A8BD95"]

# Crear gráfico de barras con etiquetas de fechas en el eje x
plt.figure(figsize=(14, 8))
plt.bar(df['Fecha'], df['Total de artículos desperdiciados'], color=colors)
plt.xlabel('Fecha')
plt.ylabel('Total de artículos desperdiciados')
plt.title('Artículos desperdiciados por fecha')
plt.xticks(df['Fecha'], df['Fecha'].dt.strftime('%d/%m/%Y'), rotation=90)
plt.grid(axis='y')

plt.show()
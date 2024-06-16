import pandas as pd
import matplotlib.pyplot as plt

# Datos
data = {
    'Fecha': ['19/1/2010', '20/1/2010', '21/1/2010', '22/1/2010', '25/1/2010', '26/1/2010', '27/1/2010', '28/1/2010', '29/1/2010',' 1/2/2010',
              ' 2/2/2010',' 3/2/2010',' 4/2/2010',' 5/2/2010',' 8/2/2010',' 9/2/2010', '10/2/2010', '11/2/2010', '12/2/2010', '15/2/2010', 
              '16/2/2010', '17/2/2010', '18/2/2010', '19/2/2010', '22/2/2010', '23/2/2010', '24/2/2010', '25/2/2010', '26/2/2010',' 1/3/2010',
              ' 2/3/2010',' 3/3/2010',' 4/3/2010',' 5/3/2010', '15/3/2010', '16/3/2010', '17/3/2010', '18/3/2010', '19/3/2010', '22/3/2010', 
              '23/3/2010', '24/3/2010', '25/3/2010', '26/3/2010', '29/3/2010', '30/3/2010', '31/3/2010', '1/4/2010'],
    'Código de día': [2, 3, 4, 5, 1, 2, 3, 4, 5, 1,
                      2, 3, 4, 5, 1, 2, 3, 4, 5, 1,
                      2, 3, 4, 5, 1, 2, 3, 4, 5, 1,
                      2, 3, 4, 5, 1, 2, 3, 4, 5, 1,
                      2, 3, 4, 5, 1, 2, 3, 4],

    'Día de la semana': ['Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 
                         'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon',
                         'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon',
                         'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon',
                         'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Thu'],
    'Sándwiches de Pan Vendidos': [5, 6, 8, 4, 3, 7, 6, 0, 3, 2,
                                   3, 4, 9, 1, 3, 8, 7, 8, 2, 3, 
                                   8, 6, 4, 4, 6, 7, 6, 5, 2, 3, 
                                   8, 4, 4, None, 6, 7, 3, 5, 2,
                                   4, 8, 4, 6, 1, 2, 6, 4, 4],
    
    'Desperdicios de Sándwiches de Pan': [3, 8, 2, 2, 0, 1, 6, 0, 4,
                                          6, 7, 4, 1, 1, 5, 0, 0, 0,
                                          0, 3, 0, 0, 2, 0, 0, 0, 0,
                                          3, 0, 2, 0, 0, 0, None, 0, 1, 3,
                                          3, 0, 2, 0, 0, 0, 1, 4, 0, 0, 0],
    
    'Envolturas Vendidas': [25, 7, 14, 5, 10, 5, 19, 7, 4, 13,
                            10, 15, 13, 6, 14, 16, 12, 19, 4, 12,
                            22, 8, 19, 10, 16, 23, 15, 22, 5, 9, 
                            21, 13, 14, None, 17, 19, 13, 15, 4, 
                            13, 14, 9, 18, 4, 9, 25, 15, 16],
    
    'Desechos de Envolturas': [5, 17, 0, 7, 0, 3, 3, 0, 9, 3, 
                               2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 
                               0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                               1, 0, 0, None, 0, 0, 0, 3, 7,
                               4, 4, 0, 1, 1, 2, 0, 0, 0],

    'Muffins Vendidos': [5, 3, 4, 5, 8, 1, 6, 6, 0, 3,
                         5, 4, 14, 2, 2, 11, 5, 12, 0,
                         6, 1, 9, 10, 4, 9, 12, 1, 8, 28,
                         5, 10, 8, 6, None, 3, 5, 3, 1, 5,
                         3, 7, 8, 3, 3, 3, 11, 1, 6],
    
    'Muffins Desperdiciados': [1, 5, 0, 0, 0, 0, 0, 1, 4, 0,
                               0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 2, 0, 0, 0, 0, 1, 0,
                               0, 2, 0, None, 0, 2, 4, 2, 2, 0,
                               0, 0, 0, 1, 0, 1, 0, 0],
    
    'Galletas Vendidas': [5, 1, 1, 3, 3, 5, 10, 0, 3, 6,
                          5, 4, 13, 1, 8, 9, 7, 9, 2, 8,
                          3, 10, 9, 4, 7, 12, 6, 4, 8, 6,
                          9, 8, 8, None, 4, 13, 6, 5, 3, 2,
                          4, 5, 3, 5, 1, 9, 9, 6],
    'Galletas Desechadas': [3, 6, 0, 1, 0, 0, 0, 0, 2, 0, 0,
                            1, 0, 1, 0, 1, 3, 0, 0, 2, 1, 1,
                            0, 0, 0, 0, 1, 0, 0, 1, 1, 2, 0,
                            None, 0, 0, 0, 2, 3, 4, 3, 4, 1,
                            1, 0, 0, 4, 0, ],
    'Vasos de Frutas Vendidos': [1, 0, 0, 3, 2, 2, 2, 0, 1,
                                 2, 1, 2, 3, 0, 1, 2, 1, 2,
                                 2, 2, 3, 1, 3, 0, 1, 4, 1,
                                 4, 0, 2, 2, 3, 2, None, 2,
                                 1, 0, 4, 1, 2, 2, 2, 2, 1,
                                 0, 4, 3, 1, ],
    'Desechos de Vasos de Frutas': [4, 3, 3, 0, 0, 0, 0, 0, 1, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
                                    0, 0, 0, None, 0, 0, 0, 0, 0, 0,
                                    2, 0, 0, 1, 1, 0, 0, 0, ],
    'Papitas Fritas Vendidas': [12, 0, 0, 20, 0, 4, 2, 20, 3, 16, 2,
                                9, 13, 10, 9, 11, 14, 4, 25, 7, 13, 11,
                                8, 14, 11, 21, 11, 10, 11, 10, 12, 9, 8,
                                None, 9, 11, 7, 8, 1, 8, 7, 7, 9, 3, 4, 9, 6, 11, ],
    'Jugos Vendidos': [8, 0, 13, 0, 5, 4, 5, 6, 4, 7,
                       0, 6, 6, 1, 2, 8, 3, 2, 2, 7,
                       5, 2, 12, 4, 2, 5, 5, 4, 21, 7,
                       7, 4, 5, None, 3, 4, 4, 5, 3, 7,
                       6, 5, 4, 2, 0, 10, 4, 3, ],
    'Refrescos vendidos': [20, 13, 23, 13, 13, 33, 15, 27, 12, 19,
                           33, 20, 29, 14, 17, 31, 24, 31, 15, 26,
                           39, 24, 35, 11, 25, 36, 33, 37, 22, 36,
                           54, 34, 43, None, 24, 48, 35, 33, 24, 30,
                           50, 45, 50, 26, 26, 55, 42, 45],
    'Cafes Vendidos': [41, 33, 34, 27, 20, 23, 32, 31, 30, 27,
                       30, 27, 26, 24, 18, 22, 21, 28, 23, 31,
                       29, 48, 25, 31, 25, 35, 33, 35, 16, 24,
                       20, 11, 21, None, 8, 8, 4, 4, 3, 5, 6, 
                       4, 13, 4, 16, 14, 10, 11],
    'Total de Refrescos y Cafes Vendidos': [61, 46, 57, 40, 33, 56, 47, 58, 42, 46,
                                            63, 47, 55, 38, 35, 53, 45, 59, 38, 57,
                                            68, 72, 60, 42, 50, 71, 66, 72, 38, 60,
                                            74, 45, 64, None, 32, 56, 39, 37, 27, 35,
                                            56, 49, 63, 30, 42, 69, 52, 56], 
    'Ventas totales': [199.95, 195.74, 102.68, 162.88, 101.76, 186.94, 120.18, 228.78, 88.02, 119.57, 172.31, 137.65,
                       197.56,.70,.97, 181.43, 125.57, 180.63, 75.87, 150.51, 177.41, 153.84, 205.36, 118.54, 138.04,
                       236.01, 149.58, 206.17, 93.1, 151.91, 217.29, 148.24, 168.08, 0, 130.77, 164.54, 121.41, 127.93,
                       61.94, 128.59, 159.23, 148.08, 164.86, 74.13, 82.96, 240.87, 151.52, 150.99, ],
    'Temperaturas Max Diaria': [36, 34, 39, 40, 36, 26, 34, 33, 20, 37,
                                38, 33, 39, 35, 31, 29, 26, 28, 30, 26,
                                29, 29, 34, 39, 36, 33, 28, 33, 35, 40,
                                39, 39, 45, 47, 48, 61, 64, 64, 65, 47,
                                62, 66, 56, 49, 56, 62, 76, 80], 
    'Total de articulos desperdiciados': [16, 39, 5, 10, 0, 4, 9, 1, 20, 9,
                                          9, 6, 1, 4, 7, 1, 3, 0, 0, 5, 1,
                                          2, 2, 2, 0, 0, 1, 4, 2, 4, 2, 4,
                                          0, None, 0, 3, 7, 10, 12, 10, 9, 4,
                                          2, 5, 7, 1, 4, 0, ]
}

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
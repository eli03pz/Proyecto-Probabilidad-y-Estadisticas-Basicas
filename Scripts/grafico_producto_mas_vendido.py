import matplotlib.pyplot as plt
import pandas as pd

# Datos de productos y sus ventas
product_data = {
    "Producto": ["Sándwiches de Pan", "Envolturas", "Muffins", "Galletas", "Vasos de Frutas", 
                "Papitas Viernestas", "Jugos", "Refrescos", "Cafés"],
    "Ventas": [221, 618, 275, 272, 80, 430, 232, 1390, 1011]
}

# Crear DataFrame
product_df = pd.DataFrame(product_data)

# Colores para las barras
colors = ["#241811", "#D4A979", "#E3C88F", "#C2C995", "#A8BD95"]

# Crear histograma de productos más vendidos
plt.figure(figsize=(14, 8))
plt.bar(product_df['Producto'], product_df['Ventas'], color=colors)
plt.xlabel('Tipos de Productos')
plt.ylabel('Frecuencia de Ventas')
plt.title('Frecuencia de Ventas de Productos')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()

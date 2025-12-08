# Importar librerías
import pandas as pd
import numpy as np

# Crear la base de datos
data = {
    "Talla_m": [1.55, 1.60, 1.62, 1.65, 1.67, 1.70, 1.72, 1.75, 1.78, 1.80, 1.85],
    "Peso_kg": [52, 55, 57, 59, 61, 65, 68, 70, 74, 79, 83]
}

df = pd.DataFrame(data)

# Calcular la correlación de Pearson
correlacion = df["Talla_m"].corr(df["Peso_kg"])
print("Coeficiente de correlación (r):", correlacion)

# Opcional: hacer gráfico de dispersión
import matplotlib.pyplot as plt

plt.scatter(df["Talla_m"], df["Peso_kg"], color='green')
plt.title("Relación entre Talla y Peso")
plt.xlabel("Talla (m)")
plt.ylabel("Peso (kg)")
plt.grid(True)
plt.show()

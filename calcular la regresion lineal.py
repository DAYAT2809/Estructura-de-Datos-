import pandas as pd
from scipy.stats import linregress

# Base de datos
data = {
    "Talla_m": [1.55, 1.60, 1.62, 1.65, 1.67, 1.70, 1.72, 1.75, 1.78, 1.80, 1.82, 1.85],
    "Peso_kg": [52, 55, 57, 59, 61, 65, 68, 70, 74, 77, 79, 83]
}

df = pd.DataFrame(data)

# Regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df["Talla_m"], df["Peso_kg"])

print(f"Ecuación de regresión: Peso = {intercept:.2f} + {slope:.2f} * Talla")
print("Coeficiente de correlación (r):", r_value)
print("Coeficiente de determinación (R²):", r_value**2)

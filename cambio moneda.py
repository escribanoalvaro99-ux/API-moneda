import urllib.request
import json
import pandas as pd

# 1. Obtención de los datos de tipos de cambio con el Euro desde la API de Frankfurter
url_api = "https://api.frankfurter.dev/v1/latest?from=EUR"
response = urllib.request.urlopen(url_api)
datos = json.loads(response.read().decode('utf-8'))

# 2. Extraer fecha y tasas de cambio
fecha = datos.get('date')
rates = datos.get('rates', {})

# 3. Crear el DataFrame con Moneda, Cambio y Fecha
df_api = pd.DataFrame(list(rates.items()), columns=['Moneda', 'Cambio'])
df_api['Fecha'] = fecha

# 4. Guardar como archivo CSV local
df_api.to_csv('cambio_monedas.csv', index=False)
print("Archivo 'cambio_monedas.csv' guardado correctamente.")
print(df_api.head())
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV desde la URL pública Raw de GitHub
url_github = "URL_RAW_DE_TU_GITHUB"  # Reemplazar con tu enlace Raw de GitHub
df = pd.read_csv(url_github)

# 2. Mostrar las primeras filas del DataFrame
print("--- PRIMERAS FILAS DEL DATAFRAME ---")
print(df.head())

# 3. Cálculo explícito de estadísticos (Mínimo, Máximo, Promedio, Desviación Estándar)
max_valor = df['Cambio'].max()
min_valor = df['Cambio'].min()
promedio_valor = df['Cambio'].mean()
std_valor = df['Cambio'].std()

moneda_max = df.loc[df['Cambio'] == max_valor, 'Moneda'].values[0]
moneda_min = df.loc[df['Cambio'] == min_valor, 'Moneda'].values[0]

print("\n--- ESTADÍSTICOS PRINCIPALES ---")
print(f"Tipo de cambio Máximo : {max_valor} ({moneda_max})")
print(f"Tipo de cambio Mínimo : {min_valor} ({moneda_min})")
print(f"Tipo de cambio Promedio: {promedio_valor:.4f}")
print(f"Desviación Estándar    : {std_valor:.4f}")

print("\n--- RESUMEN ESTADÍSTICO COMPLETO (describe) ---")
print(df.describe())

# 4. Creación de la gráfica de barras (primeras 10 monedas)
df_top10 = df.head(10)

plt.figure(figsize=(10, 5))
plt.bar(df_top10['Moneda'], df_top10['Cambio'], color='skyblue', edgecolor='black')
plt.xlabel('Moneda', fontsize=12)
plt.ylabel('Tipo de Cambio (respecto al EUR)', fontsize=12)
plt.title('Top 10 Monedas - Tipo de Cambio frente al Euro', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()
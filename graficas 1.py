import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ruta_csv = r'C:/Users/Luizl/Downloads/Raw Data.csv'
a = pd.read_csv(ruta_csv, sep='\t')

# Limpiar nombres de columnas (eliminar comillas y espacios)
a.columns = a.columns.str.strip().str.replace('"', '')

# Verificar los nombres reales de las columnas
print("Columnas detectadas:", a.columns.tolist())

x = a['Linear Acceleration x (m/s^2)']
y = a['Linear Acceleration y (m/s^2)']
z = a['Linear Acceleration z (m/s^2)']
h = a['Absolute acceleration (m/s^2)']
t = a['Time (s)']

plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t, x, color='green')
plt.grid(True)
plt.xlabel('t(s)')
plt.ylabel('a(m/s²)')
plt.title('Aceleración en el eje x')

plt.subplot(4, 1, 2)
plt.plot(t, y, color='blue')
plt.grid(True)
plt.xlabel('t(s)')
plt.ylabel('a(m/s²)')
plt.title('Aceleración en el eje y')

plt.subplot(4, 1, 3)
plt.plot(t, z, color='orange')
plt.grid(True)
plt.xlabel('t(s)')
plt.ylabel('a(m/s²)')
plt.title('Aceleración en el eje z')

plt.subplot(4, 1, 4)
plt.plot(t, h, color='red')
plt.grid(True)
plt.xlabel('t(s)')
plt.ylabel('a(m/s²)')
plt.title('Aceleración total')

plt.tight_layout()

plt.show()
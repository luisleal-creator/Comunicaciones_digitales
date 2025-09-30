import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

documento_csv = r'C:/Users/Luizl/Downloads/Amplitudes.csv'
a = pd.read_csv(documento_csv, sep='\t')

# Limpiar nombres de columnas (eliminar comillas y espacios)
a.columns = a.columns.str.strip().str.replace('"', '')

# Verificar los nombres reales de las columnas
print("Columnas detectadas:", a.columns.tolist())

dB = a['Sound pressure level (dB)']
t = a['Time (s)']

plt.figure(figsize=(12, 10))

plt.plot(t, dB, color='Red')
plt.grid(True)
plt.xlabel('t(s)')
plt.ylabel('NPS(dB)')


plt.tight_layout()

plt.show()
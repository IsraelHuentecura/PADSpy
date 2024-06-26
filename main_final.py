# Código del main
from PADSpy.modulo1 import MatrizDeAdyacencia
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer la matriz de adyacencia
matriz_original = pd.read_csv('matriz_adjacencia.csv')


nombre_de_variables = matriz_original.columns[1:]
matriz_original = matriz_original.fillna(0).drop(matriz_original.columns[0], axis=1).to_numpy().T
matriz_original = np.array(matriz_original)
# Agregar en la diagonal principal -3
np.fill_diagonal(matriz_original, -3)

n_variables = matriz_original.shape[0]

# Parametros de entrada
n_simulaciones = 10000
perturbacion = 0.001
vector_intervencion = np.array([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0])
objeto_matriz = MatrizDeAdyacencia(matriz_original, vector_intervencion)
matriz_con_intervencion = objeto_matriz.add_vector_intervencion()
result = objeto_matriz.get_ultima_columna_post_intervencion()


# Test de robustez
robustez = objeto_matriz.probar_robustez(n_simulaciones, perturbacion)

# Graficar el promedio de las intervenciones simuladas versus la intervención original
bar_width = 0.35
plt.figure(figsize=(9, 9))
r1 = np.arange(len(vector_intervencion))
r2 = [x + bar_width for x in r1]

print(f'Promedio intervenciones simuladas: {robustez}')
print(f'Intervención original: {result}')
plt.bar(r1, result, width=bar_width, tick_label=nombre_de_variables, label='Intervención original')
plt.bar(r2, robustez, width=bar_width, label='Promedio intervenciones simuladas')

plt.xticks(rotation=45)
plt.tight_layout()
plt.title('Robustez del modelo')
plt.xlabel('Variables')
plt.ylabel('Valores de intervención')
plt.legend()
plt.show()
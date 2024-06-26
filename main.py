from PADSpy.modulo1 import MatrizDeAdyacencia
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Leer la matriz de adyacencia
matriz_original = pd.read_csv('matriz_adjacencia.csv')
nombre_de_variables = matriz_original.columns
nombre_de_variables = nombre_de_variables[1:]
# Todos los nan los reemplazamos por 0
matriz_original = matriz_original.fillna(0)
# Borrar la primera columnas y la fila de los nombres
matriz_original = matriz_original.drop(matriz_original.columns[0], axis=1)
# Pasar a numpy
matriz_original = matriz_original.to_numpy()
# Transponer la matriz
matriz_original = matriz_original.T

# Prueba
#matriz_original = np.array([[0,0,1],[0,0,0],[0,1,0]])

# Agregar en la diagonal principal -1
np.fill_diagonal(matriz_original, -3)
print(matriz_original)

n_variables = matriz_original.shape[0]
# Vector de intervención de -1 a 1 en este caso son 14
vector_intervencion = [0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0]
vector_intervencion = np.array(vector_intervencion)
objeto_matriz = MatrizDeAdyacencia(matriz_original, vector_intervencion)

# Agregamos el vector de intervención y la fila de ceros
matriz_con_intervencion = objeto_matriz.agregar_vector_intervencion()
print("Matriz con vector de intervención y fila de ceros:")
print(matriz_con_intervencion)

# Calculamos la inversa negativa de la matriz original y de la matriz con intervención
inversa_negativa_original = objeto_matriz.obtener_inversa_negativa()
inversa_negativa_con_intervencion = MatrizDeAdyacencia(matriz_con_intervencion[:-1, :-1], vector_intervencion).obtener_inversa_negativa()
print("\nInversa negativa de la matriz original:")
print(inversa_negativa_original)
print("\nInversa negativa de la matriz con intervención:")
print(inversa_negativa_con_intervencion)

# Extraer la última columna de la matriz con intervención
ultima_columna = inversa_negativa_con_intervencion[:, -1]


# Tamaño de la figura
plt.figure(figsize=(15, 9))

# Graficar la última columna de la matriz con intervención como gráfico de barras

plt.bar(nombre_de_variables, ultima_columna)
plt.title('Intervención sobre las variables')
# Rotar los nombres de las variables para que no se superpongan
plt.xticks(rotation=45)
# Cuidar que se vean los nombres de las variables enteros y no se corten
plt.tight_layout()
plt.xlabel('Variables')
plt.ylabel('Valores de intervención')
plt.show()

# Probar la robustez de la matriz original
vectores_intervenciones_simuladas = objeto_matriz.probar_robustez()
# Graficar el promedio de las intervenciones simuladas versus la intervención original para ver la robustez del modelo
# Poniendo las barras una al lado de otra para comparar
promedio_intervenciones_simuladas = np.mean(vectores_intervenciones_simuladas, axis=0)

# Ancho de cada barra
bar_width = 0.35
plt.figure(figsize=(16, 9))

# Posiciones de las barras
r1 = np.arange(len(vector_intervencion))
r2 = [x + bar_width for x in r1]

plt.bar(r1, ultima_columna, width=bar_width, tick_label=nombre_de_variables, label='Intervención original')
plt.bar(r2, promedio_intervenciones_simuladas, width=bar_width, label='Promedio intervenciones simuladas')


# Rotar los nombres de las variables para que no se superpongan
plt.xticks(rotation=45)
plt.tight_layout()
plt.title('Robustez del modelo')
plt.xlabel('Variables')
plt.ylabel('Valores de intervención')
plt.legend()
# Abrir la ventana de visualización en un tamaño adecuado
plt.show()

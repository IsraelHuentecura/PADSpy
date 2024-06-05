from PADSpy.modulo1 import MatrizDeAdyacencia
import numpy as np

# Ejemplo de uso
matriz_original = np.array([[12, 1, 2], [1, 3, 76], [0, 5, 4]])
vector_intervencion = np.array([0.5, -0.2, 0.1])
objeto_matriz = MatrizDeAdyacencia(matriz_original)

# Agregamos el vector de intervención y la fila de ceros
matriz_con_intervencion = objeto_matriz.agregar_vector_intervencion(vector_intervencion)
print("Matriz con vector de intervención y fila de ceros:")
print(matriz_con_intervencion)

# Calculamos la inversa negativa de la matriz original y de la matriz con intervención
inversa_negativa_original = objeto_matriz.obtener_inversa_negativa()
inversa_negativa_con_intervencion = MatrizDeAdyacencia(matriz_con_intervencion).obtener_inversa_negativa()
print("\nInversa negativa de la matriz original:")
print(inversa_negativa_original)
print("\nInversa negativa de la matriz con intervención:")
print(inversa_negativa_con_intervencion)

# Graficar la ultima columna de la matriz con intervencion como grafico de barras
import matplotlib.pyplot as plt
plt.bar(range(len(vector_intervencion)), vector_intervencion)
plt.show()

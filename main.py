from PADSpy.modulo1 import MatrizDeAdyacencia
import numpy as np

# Ejemplo de uso
matriz_original = np.array([[0, 2, 2], [1, 0, 1], [0, 1, 0]])
objeto_matriz = MatrizDeAdyacencia(matriz_original)
inversa_negativa = objeto_matriz.obtener_inversa_negativa()

print("Matriz original:")
print(matriz_original)
print("\nInversa negativa:")
print(inversa_negativa)
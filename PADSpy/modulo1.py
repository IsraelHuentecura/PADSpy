import numpy as np

class MatrizDeAdyacencia:
    def __init__(self, matriz):
        # Verificamos que la matriz sea cuadrada
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("La matriz debe ser cuadrada (misma cantidad de filas y columnas)")

        self.matriz = matriz

    def obtener_inversa_negativa(self):
        # Calculamos la inversa negativa de la matriz
        inversa_negativa = -np.linalg.inv(self.matriz)
        return inversa_negativa

    def agregar_vector_intervencion(self, vector):
        # Verificamos que el vector tenga la misma cantidad de elementos que la matriz
        if len(vector) != self.matriz.shape[0]:
            raise ValueError("El vector de intervención debe tener la misma cantidad de elementos que la matriz")

        # Agregamos el vector de intervención al final de las columnas
        matriz_con_intervencion = np.hstack((self.matriz, vector.reshape(-1, 1)))

        # Agregamos una fila de ceros al final para mantener la matriz cuadrada
        matriz_con_fila_ceros = np.vstack((matriz_con_intervencion, np.zeros(matriz_con_intervencion.shape[1])))

        # Agregamos el valor -1 al final del vector de intervención
        matriz_con_fila_ceros[-1, -1] = -1

        return matriz_con_fila_ceros



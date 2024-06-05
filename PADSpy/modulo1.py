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


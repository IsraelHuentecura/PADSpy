import numpy as np
import matplotlib.pyplot as plt

class MatrizDeAdyacencia:
    def __init__(self, matriz, vector):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("La matriz debe ser cuadrada (misma cantidad de filas y columnas)")
        # Evaluar si la matriz es estable
        if not np.all(np.linalg.eigvals(matriz) < 0):
            raise ValueError(f"La matriz no es estable: {np.linalg.eigvals(matriz)}")

        self.matriz = matriz
        self.vector_intervencion = vector

    def get_inversa_negativa(self):
        return -np.linalg.inv(self.matriz)

    def add_vector_intervencion(self):
        if len(self.vector_intervencion) != self.matriz.shape[0]:
            raise ValueError("El vector de intervención debe tener la misma cantidad de elementos que la matriz")

        matriz_con_intervencion = np.hstack((self.matriz, self.vector_intervencion.reshape(-1, 1)))
        matriz_con_fila_ceros = np.vstack((matriz_con_intervencion, np.zeros((1, matriz_con_intervencion.shape[1]))))
        matriz_con_fila_ceros[-1, -1] = -1

        return matriz_con_fila_ceros
    
    def get_ultima_columna_post_intervencion(self):
        matriz_con_intervencion = self.add_vector_intervencion()
        inversa_negativa_con_intervencion = -np.linalg.inv(matriz_con_intervencion)
        return inversa_negativa_con_intervencion[:-1, -1]
    
    
    def probar_robustez(self, n_simulaciones=1000, perturbacion=0.00001):
        lista_de_ultimas_columnas_perturbadas = []
        for i in range(n_simulaciones):
            matriz_con_intervencion = self.add_vector_intervencion()
            matriz_perturbacion = np.random.normal(0, perturbacion, size=matriz_con_intervencion.shape)
            suma_matriz_ya_perturbada = matriz_con_intervencion + matriz_perturbacion
            ultima_columna_perturbada = -np.linalg.inv(suma_matriz_ya_perturbada)[:-1, -1]
            lista_de_ultimas_columnas_perturbadas.append(ultima_columna_perturbada)
        varianza_ultimas_columnas_perturbadas = np.var(lista_de_ultimas_columnas_perturbadas, axis=0)
        return np.mean(lista_de_ultimas_columnas_perturbadas, axis=0), varianza_ultimas_columnas_perturbadas

  
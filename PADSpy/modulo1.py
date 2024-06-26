import numpy as np
import matplotlib.pyplot as plt

class MatrizDeAdyacencia:
    def __init__(self, matriz,vector):
        if matriz.shape[0] != matriz.shape[1]:
            raise ValueError("La matriz debe ser cuadrada (misma cantidad de filas y columnas)")
        # Evaluar si la matriz es estable
        if not np.all(np.linalg.eigvals(matriz) < 0):
           # print("Valores prop")
          #  raise print(np.linalg.eigvals(matriz))
            raise ValueError("La matriz no es estable")

        self.matriz = matriz
        self.vector_intervencion = vector

    def obtener_inversa_negativa(self):
        inversa_negativa = -np.linalg.inv(self.matriz)
        return inversa_negativa

    def agregar_vector_intervencion(self):
        if len(self.vector_intervencion) != self.matriz.shape[0]:
            raise ValueError("El vector de intervención debe tener la misma cantidad de elementos que la matriz")

        matriz_con_intervencion = np.hstack((self.matriz, self.vector_intervencion.reshape(-1, 1)))
        matriz_con_fila_ceros = np.vstack((matriz_con_intervencion, np.zeros(matriz_con_intervencion.shape[1])))
        matriz_con_fila_ceros[-1, -1] = -1

        return matriz_con_fila_ceros

    def probar_robustez(self, num_muestras=1000):
        """Probar la robustez de la matriz original variando la matriz de adyacencia segun una distribución normal y calculando la inversa negativa de cada una.
        

        Args:
            num_muestras (int, optional): _description_. Defaults to 1000.
            
        """
        resultados = []
        matriz_original = self.matriz
        for prueba in range(num_muestras):
            variacion_matriz_adyacencia = np.random.normal(loc=0, scale=0.00000001, size=matriz_original.shape)
            # Sumar la matriz original a la variación
            variacion_matriz_adyacencia  = variacion_matriz_adyacencia + matriz_original
            
            # Matriz original obsoluta
            matriz_original_valor_obsolulto = np.absolute(matriz_original)
            # Poner en 1 en la diagonal principal
            np.fill_diagonal(matriz_original_valor_obsolulto, 1)
            #return print(f"PRUEBA MATRIZ:{matriz_original_valor_obsolulto}")
            # Multiplicar producto hadamard
            variacion_matriz_adyacencia_sin_generar_cambios_estructurales = np.multiply(variacion_matriz_adyacencia, matriz_original_valor_obsolulto)
#            return print(f"PRUEBA MATRIZ:{variacion_matriz_adyacencia_sin_generar_cambios_estructurales}")
            # no en lo numerico si no en el formato
            #array_de_numeros = [numero for numero in variacion_matriz_adyacencia_generar_cambios_estructurales]
            # Array a matriz
            #matriz_formato = np.array(variacion_matriz_adyacencia_sin_generar_cambios_estructurales)
            matriz_formato = variacion_matriz_adyacencia_sin_generar_cambios_estructurales
            matriz_con_intervencion = np.hstack((matriz_formato, self.vector_intervencion.reshape(-1, 1)))
            matriz_con_fila_ceros = np.vstack((matriz_con_intervencion, np.zeros(matriz_con_intervencion.shape[1])))
            matriz_con_fila_ceros[-1, -1] = -1 
            # Calcular la inversa negativa de la matriz con intervención
            inversa_negativa_con_intervencion = -np.linalg.inv(matriz_con_fila_ceros)
            
            # Solo nos interesa la última columna de la matriz que corresponde a la intervención
            resultados.append(inversa_negativa_con_intervencion[:-1, -1])
            #return print(f"PRUEBA:{inversa_negativa_con_intervencion[:-1, -1]}")
            
        
        return resultados
    


import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PADSpy.modulo1 import MatrizDeAdyacencia

# Usar todo el espacio disponible
st.set_page_config(layout="wide")

# Configurar Streamlit
st.title("Simulador de Intervención en nuestro sistema")

# Leer la matriz de adyacencia
matriz_original = pd.read_csv('matriz_adjacencia.csv')

nombre_de_variables = matriz_original.columns[1:]
matriz_original = matriz_original.fillna(0).drop(matriz_original.columns[0], axis=1).to_numpy().T
matriz_original = np.array(matriz_original)
# Agregar en la diagonal principal -3
np.fill_diagonal(matriz_original, -3)

n_variables = matriz_original.shape[0]

# Parámetros de entrada en la barra lateral
st.sidebar.header("Parámetros de Entrada")
n_simulaciones = st.sidebar.slider("Número de Simulaciones", min_value=1000, max_value=20000, step=1000, value=10000)
perturbacion = st.sidebar.slider("Perturbación", min_value=0.00000001, max_value=1.0, step=0.0001, value=0.001)

# Crear el vector de intervención
vector_intervencion = np.zeros(n_variables)
for i in range(n_variables):
    intervencion = st.sidebar.slider(f"Intervención en {nombre_de_variables[i]}", min_value=-1.0, max_value=1.0, step=0.1, value=0.0)
    vector_intervencion[i] = intervencion

# Ejecutar la simulación con los parámetros seleccionados
objeto_matriz = MatrizDeAdyacencia(matriz_original, vector_intervencion)
matriz_con_intervencion = objeto_matriz.add_vector_intervencion()
result = objeto_matriz.get_ultima_columna_post_intervencion()

# Test de robustez
robustez, varianza = objeto_matriz.probar_robustez(n_simulaciones, perturbacion)

# Calcular el error estándar de la media (SEM)
sem = np.sqrt(varianza / n_simulaciones)

# Mostrar resultados
st.subheader("Resultados")

# Graficar los resultados con Plotly
fig = go.Figure()

bar_width = 0.35
r1 = np.arange(len(vector_intervencion))
r2 = [x + bar_width for x in r1]

fig.add_trace(go.Bar(
    x=nombre_de_variables,
    y=result,
    name='Intervención original',
    marker_color='indianred'
))

fig.add_trace(go.Bar(
    x=nombre_de_variables,
    y=robustez,
    name='Promedio intervenciones simuladas',
    marker_color='lightsalmon',
    error_y=dict(
        type='data',
        array=sem,
        visible=True
    )
))

fig.update_layout(
    title='Robustez del modelo',
    xaxis_tickangle=-45,
    xaxis_title='Variables',
    yaxis_title='Valores de intervención',
    barmode='group'
)

if sum(vector_intervencion) == 0:
    st.write("No se ha seleccionado ninguna intervención")
else:
    st.plotly_chart(fig, use_container_width=True) 
    st.write(f"Promedio intervenciones simuladas: {robustez}")
    st.write(f"Varianza de las intervenciones simuladas: {varianza}")
    st.write(f"Error estándar de la media: {sem}")
    st.write(f"Intervención original: {result}")

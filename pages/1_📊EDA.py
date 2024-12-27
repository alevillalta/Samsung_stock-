import pandas as pd
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.eda import plot_histogram, plot_heatmap

# Carga el DataFrame
@st.cache_data
def load_data():
    return pd.read_csv("data/samsung_stock.csv") 

# Configuración de la página
st.title("Análisis Exploratorio de Datos")

# Carga de datos 
df = load_data()

# Información básica del conjunto de datos
st.header("Aspectos Básicos del Conjunto de Datos")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Número de Filas", value=df.shape[0], delta=None)
    with col2:
        st.metric(label="Número de Columnas", value=df.shape[1], delta=None)
    with col3:
        missing_values = df.isnull().any().sum()
        st.metric(label="Valores Perdidos", value="Sí" if missing_values > 0 else "No", delta=None)

# Mostrar gráficos
st.header("Histograma de Samsung Stock")
histogram_fig = plot_histogram(df)
st.plotly_chart(histogram_fig)

st.header("Matriz de Correlación")
heatmap_fig = plot_heatmap(df)
st.pyplot(heatmap_fig)  

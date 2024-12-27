import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide")

st.title("Proyecto Final ✅")

st.markdown("""
## Bienvenido
            Este proyecto incluye las siguientes páginas:
            """)

col1, col2 =st.columns([2, 2])

with col1:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image ("utils/lupa.jpg", width=250)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader ("EDA: Análisis exploratorio de datos")
    st.markdown("Examina los datos y descubre patrones interesantes.")
   
col3, col4 = st.columns ([2, 2])

with col3:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st. image("utils/idea.jpg", width=250)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st. subheader ("Hipótesis: Visualización de hipótesis propuestas")
    st.markdown ("Evalúa diferentes hipótesis mediante gráficos.")

col5, col6 = st.columns([2,2])

with col5:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st. image("utils/brain.jpg", width=250)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st. subheader ("Modelo: Predicciones con un modelo de regresion lineal")
    st.markdown ("Genera predicciones y evalua el desempeño del modelo.")
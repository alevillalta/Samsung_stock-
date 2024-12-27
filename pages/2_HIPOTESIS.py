import streamlit as st
import os
import sys
import pandas as pd

# Agregar el directorio src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.hipotesis import hipotesis_1, hipotesis_2, hipotesis_3, hipotesis_4, grafico1_hipotesis_5, grafico2_hipotesis_5, load_data
except ImportError as e:
    st.error(f"Error al importar módulos de hipótesis: {e}")
    st.stop()

# Cargar datos
df = load_data()
df.rename(columns={"Unnamed: 0": "Date"}, inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values("Date", inplace=True)
df["volatilidad"] = df["High"] - df["Low"]
df["Retorno diario"] = df["Adj Close"].pct_change()
df["Caida"] = df["Retorno diario"] < -0.05
caidas = df[df["Caida"]]
df["maximo"] = df["Adj Close"].cummax()
df["alto"] = df["Adj Close"] == df["maximo"]

# Configurar la página
st.title("Análisis Exploratorio de Hipótesis")

# Hipótesis 1
st.header("HIPÓTESIS 1")
st.subheader("El precio de las acciones de Samsung sigue una tendencia alcista a largo plazo")
fig1 = hipotesis_1(df)
st.pyplot(fig1)

st.write("Según lo observado en el gráfico, la hipótesis propuesta es correcta, ya que se observa una tendencia alcista sostenida. También destaca la volatilidad del mercado en ciertos períodos, lo que sugiere que el precio de las acciones está influenciado tanto por factores internos como externos.")

# Hipótesis 2
st.header("HIPÓTESIS 2")
st.subheader("Los precios de las acciones son más estables durante los meses de invierno que en el verano")
fig2 = hipotesis_2(df)
st.pyplot(fig2)

st.write("Según lo observado en el gráfico, la volatilidad es similar en invierno y verano, sin diferencias estacionales significativas, pero con valores extremos en ambas estaciones.")

# Hipótesis 3
st.header("HIPÓTESIS 3")
st.subheader("Las acciones de Samsung tienden a recuperarse rápidamente después de caídas fuertes (>5%)")
fig3 = hipotesis_3(df, caidas)
st.pyplot(fig3)

st.write("Según lo observado en el gráfico, las caídas diarias de más del 5% son infrecuentes y están asociadas a eventos importantes, reflejando la sensibilidad del mercado.")

# Hipótesis 4
st.header("HIPÓTESIS 4")
st.subheader("Durante eventos de crisis económica global, el precio de las acciones de Samsung disminuye")
crisis = [("2008-09-01", "2009-06-30"), ("2020-03-01", "2020-12-30")]
fig4 = hipotesis_4(df, crisis)
st.pyplot(fig4)

st.write("Según el gráfico observado, las crisis globales (2008-2009 y 2020) generaron caídas pronunciadas en los precios, confirmando la vulnerabilidad del mercado a factores macroeconómicos.")

#hipotesis 5
#grafico 1
st.header("HIPÓTESIS 5")
st.subheader("El volumen de transacciones aumenta significativamente en días donde el precio de las acciones alcanza máximos históricos")
fig5 = grafico1_hipotesis_5(df)
st.pyplot(fig5)

#grafico2
fig6 = grafico2_hipotesis_5(df)
st.pyplot(fig6)

st.write("La hipótesis sugiere que el volumen de transacciones aumenta significativamente en máximos históricos. El primer gráfico muestra que estos máximos coinciden con incrementos en el precio ajustado, y el segundo gráfico confirma que el volumen es mayor en estos días, validando la hipótesis.")
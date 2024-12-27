import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("data/samsung_stock.csv")

# Funciones de análisis e hipótesis
def hipotesis_1(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["Date"], df["Adj Close"], label="Precio Ajustado", color="skyblue")
    ax.set_title("Tendencia del Precio Ajustado de Samsung")
    ax.set_xlabel("Año")
    ax.set_ylabel("Precio Ajustado")
    ax.legend()
    ax.grid()
    return fig

def hipotesis_2(df):
    invierno = df[df["Date"].dt.month.isin([12, 1, 2])]
    verano = df[df["Date"].dt.month.isin([6, 7, 8])]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot([invierno["volatilidad"], verano["volatilidad"]], labels=["Invierno", "Verano"], patch_artist=True)
    ax.set_title("Comparación de Volatilidad: Invierno vs Verano")
    ax.set_ylabel("Volatilidad (High - Low)")
    ax.grid()
    return fig

def hipotesis_3(df, caidas):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["Date"], df["Adj Close"], label="Precio Ajustado", color="skyblue")
    ax.scatter(caidas["Date"], caidas["Adj Close"], color="red", label="Caída >5%")
    ax.set_title("Caídas Significativas y Recuperaciones")
    ax.set_xlabel("Año")
    ax.set_ylabel("Precio Ajustado")
    ax.legend()
    ax.grid()
    return fig

def hipotesis_4(df, crisis):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["Date"], df["Adj Close"], label="Precio Ajustado", color="skyblue")
    for start, end in crisis:
        ax.axvspan(pd.to_datetime(start), pd.to_datetime(end), color="yellow", alpha=0.4, label=f"Crisis: {start} - {end}")
    ax.set_title("Impacto de Crisis en el Precio de Samsung")
    ax.set_xlabel("Año")
    ax.set_ylabel("Precio Ajustado")
    ax.legend()
    ax.grid()
    return fig

def grafico1_hipotesis_5(df):
    
    # Crear una columna que indica si es un máximo histórico
    df["alto"] = df["Adj Close"] == df["Adj Close"].cummax()

    # Gráfico de precios ajustados con máximos históricos
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.plot(df.index, df["Adj Close"], label="Precio Ajustado")
    ax.scatter(
        df.index[df["alto"]],
        df["Adj Close"][df["alto"]],
        color="red",
        label="Máximos Históricos",
        s=50,
        alpha=0.7,
    )
    ax.set_title("Precio Ajustado con Máximos Históricos Destacados")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio Ajustado")
    ax.legend()
    ax.grid()

    return fig

def grafico2_hipotesis_5(df):
     # Crear una columna que indica si es un máximo histórico
    df["alto"] = df["Adj Close"] == df["Adj Close"].cummax()

    # Gráfico de caja del volumen de transacciones
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.boxplot(
        [df[df["alto"]]["Volume"], df[~df["alto"]]["Volume"]],
        labels=["Máximos Históricos", "Otros Días"],
        patch_artist=True,
    )
    ax.set_title("Volumen de Transacciones en Máximos Históricos")
    ax.set_ylabel("Volumen")
    ax.grid()

    return fig
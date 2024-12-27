### aqui va todo el codigo de eda
import sys
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px

def plot_histogram(df):
    fig = px.histogram(
        data_frame=df,
        x='High',
        title="Histograma de Samsung Stock",
    )
    fig.update_layout(
        yaxis_title="Frecuencia",
        xaxis_title="Precios"
    )
    return fig

import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(df):
    numeric_df = df.select_dtypes(include=['number'])  
    correlation_matrix = numeric_df.corr()  # Calcula la matriz de correlación

    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    
    return heatmap.get_figure()  

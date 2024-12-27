from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import streamlit as st

# Carga el DataFrame
@st.cache_data
def load_data():
    data = pd.read_csv("data/samsung_stock.csv")
    st.write("Vista previa del conjunto de datos cargados desde el archivo local:")
    st.dataframe(data.head())
    return data

# Cargar los datos
data = load_data()

# Convertir la columna de fecha y establecer como índice
data['Date'] = pd.to_datetime(data['Unnamed: 0'])  # Convertir fecha
data.set_index('Date', inplace=True)  # Usar fecha como índice

# Definir variables
X = data[['Open', 'High', 'Low', 'Volume']]  
y = data['Close']  

# Dividir datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

# Crear y entrenar el modelo
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Mostrar resultados
st.write("Resultados del modelo:")
st.write(f"Error cuadrático medio (MSE): {mse:.2f}")
st.write(f"Coeficiente de determinación (R²): {r2:.2f}")

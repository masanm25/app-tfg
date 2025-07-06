import streamlit as st
import pandas as pd

# Título de la app
st.set_page_config(page_title="Predicción de Fístula Pancreática", layout="wide")
st.title("Sistema experto para la predicción de fístula pancreática")

# Subida de archivo
st.sidebar.header("Sube tu archivo de datos")
archivo = st.sidebar.file_uploader("Selecciona un archivo Excel o CSV", type=["csv", "xlsx"])

# Procesamiento del archivo
@st.cache_data
def cargar_datos(archivo):
    if archivo is not None:
        if archivo.name.endswith(".csv"):
            return pd.read_csv(archivo)
        elif archivo.name.endswith(".xlsx"):
            return pd.read_excel(archivo)
    return None

# Mostrar datos
df = cargar_datos(archivo)
if df is not None:
    st.success("Archivo cargado correctamente")

    # Estructura del dataset
    st.subheader("Estructura del dataset")
    st.write(f"El dataset tiene **{df.shape[0]}** filas y **{df.shape[1]}** columnas.")

    # Primeras filas
    st.subheader("Primeras filas del dataset")
    st.dataframe(df.head())

    # Información de las variables
    st.subheader("Tipos de variables y nulos")
    info_df = pd.DataFrame({
        'Tipo de dato': df.dtypes,
        'Nulos': df.isna().sum(),
        'Valores únicos': df.nunique()
    })
    st.dataframe(info_df.reset_index().rename(columns={'index': 'Variable'}))
else:
    st.info("Espera a subir un archivo para comenzar el análisis.")

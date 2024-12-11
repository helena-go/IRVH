import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Configuración de la página
st.title("Análisis de Rentabilidad Hotelera (Opción 1)")

# Cargar los datos
st.write("Cargando datos...")
excel_file = pd.ExcelFile("C:/Users/betif/OneDrive/Escritorio/USC/3o IA/Proyecto/TID_EHC_G7/Datos generales competencia Madrid.xlsx")
datos_generales = pd.read_excel(excel_file, sheet_name='Datos generales competidores')
precios_competidores = pd.read_excel(excel_file, sheet_name='Precios de los competidores')
df_ingresos = pd.read_excel('C:/Users/betif/OneDrive/Escritorio/USC/3o IA/Proyecto/TID_EHC_G7/Ingresos hoteles Madrid.xlsx')

st.write("Datos cargados con éxito.")

# Procesar datos (similar al ejemplo anterior)
datos_generales['hot_id'] = datos_generales['hot_id'].astype(int)
precios_competidores['hot_id'] = precios_competidores['hot_id'].astype(int)
df_inicial = pd.merge(datos_generales, precios_competidores, on='hot_id', how='inner')

df_ingresos_filtrado = df_ingresos[df_ingresos['date_gen'] == df_ingresos['date_eval']].copy()
df_ingresos_filtrado['week'] = pd.to_datetime(df_ingresos_filtrado['date_eval']).dt.isocalendar().week
df_ingresos_filtrado['year'] = pd.to_datetime(df_ingresos_filtrado['date_eval']).dt.year
df_ingresos_agrupados = df_ingresos_filtrado.groupby(['hot_id', 'year', 'week'])['ingresos'].mean().reset_index()

resultado = pd.merge(df_inicial, df_ingresos_agrupados, how='left', on=['hot_id'])
resultado['ingresos'] = resultado.groupby('hot_id')['ingresos'].transform(lambda x: x.fillna(x.mean()))
max_ingresos = resultado['ingresos'].max()
resultado['Satisfaccion'] = (resultado['ingresos'] / max_ingresos * 10).clip(upper=9).round(1) / 10
resultado['IR'] = (resultado['ingresos'] / resultado['num_rooms']) * resultado['Satisfaccion']

# Mostrar gráficos
st.write("Distribución del Índice de Rentabilidad (IR):")
fig, ax = plt.subplots()
resultado['IR'].plot(kind='hist', bins=50, title='Distribución de IR', ax=ax)
ax.spines[['top', 'right']].set_visible(False)
st.pyplot(fig)

# Continuar con más análisis...

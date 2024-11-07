import streamlit as st


# Cargar el archivo CSS desde el repositorio de GitHub (reemplaza con la URL de tu archivo CSS)
st.markdown(
    """
    <style>
    @import url('https://raw.githubusercontent.com/usuario/repositorio/main/styles.css');
    </style>
    """, 
    unsafe_allow_html=True
)

# Aquí va el resto de tu aplicación Streamlit
st.title("Análisis de Rentabilidad en la expansión hotelera.")
st.header("Eurostars Hotel Company.")
st.write("Visualización de los datos.")

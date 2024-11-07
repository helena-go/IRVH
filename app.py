import streamlit as st


# Cargar el archivo CSS desde el repositorio de GitHub (reemplaza con la URL de tu archivo CSS)
st.markdown(
    """
    <style>
    @import url('https://github.com/helena-go/IRVH/blob/88633a84cc2fbb54c25797fc75bc238da64c940c/styles.css');
    </style>
    """, 
    unsafe_allow_html=True
)

# Aquí va el resto de tu aplicación Streamlit
st.title("Análisis de Rentabilidad en la expansión hotelera.")
st.header("Eurostars Hotel Company.")
st.write("Visualización de los datos.")

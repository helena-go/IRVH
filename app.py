import streamlit as st


st.set_page_config(
    page_title="Análisis de Rentabilidad Hotelera",  # Título en la pestaña
    page_icon="🏨",  # Ícono en la pestaña, puedes usar emojis o enlaces de imágenes
    layout="wide"  # Configuración de ancho de página, puede ser "centered" o "wide"
)



# Cambiar el fondo de la página a negro
st.markdown("""
    <style>
        body {
            background-color: black !important;
            color: white; /* Cambiar el color del texto a blanco */
        }
    </style>
""", unsafe_allow_html=True)

#COLOR DE TEXTO

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: White;">Análisis de Rentabilidad Hotelera 🏨</h1>
        <p style="font-size:18px; color: #34495E;">Explora la rentabilidad de ubicaciones para la expansión hotelera con visualizaciones interactivas</p>
    </div>
    """,
    unsafe_allow_html=True
)



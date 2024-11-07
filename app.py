import streamlit as st


st.set_page_config(
    page_title="Análisis de Rentabilidad Hotelera",  # Título en la pestaña
    page_icon="🏨",  # Ícono en la pestaña, puedes usar emojis o enlaces de imágenes
    layout="wide"  # Configuración de ancho de página, puede ser "centered" o "wide"
)


import streamlit as st

# Cambiar el fondo de la página y el color del texto sin usar un archivo CSS externo.
#Más adelante miramos como meterlo en el css.
st.markdown("""
    <style>
        /* Cambiar el fondo de la página a negro */
        html, body {
            background-color: black !important;
            color: white !important;
        }
        
       /* Usar la fuente 'Playfair Display' para los títulos */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Playfair Display', serif;
            color: black !important;
        }


        /* Cambiar el color de los botones */
        button {
            background-color: white !important;
            color: black !important;
        }

        /* Cambiar el color de los inputs y text areas */
        input, textarea {
            background-color: black !important;
            color: white !important;
            border: 1px solid gold !important;
            font-family: 'Playfair Display', serif;
        }
    </style>
""", unsafe_allow_html=True)

#TITULO Y SUBTÍTULO.

# Ejemplo de contenido en la página
st.title("Análisis de rentabilidad hotelera 🏨")
st.markdown("""
    <style>
        h1 {
            text-align: center;  /* Centrar los títulos */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-style: italic; font-size: 18px; '>Eurostars hotel company</h2>", unsafe_allow_html=True)

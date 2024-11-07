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


#IMAGENES:

#Imagen zona superior izquierda
# Insertar la imagen en la parte superior izquierda usando HTML
# Insertar dos imágenes, una más arriba que la otra en la parte superior izquierda usando HTML y CSS
# Primera imagen
st.image("https://tse2.mm.bing.net/th?id=OIP.-wMbVBuxXB9Cf2AQZTrdkAHaEK&pid=Api", width=100)

# Añadir un espacio en blanco para separar las imágenes
st.markdown("<br>", unsafe_allow_html=True)  # Esto agrega un salto de línea

# Segunda imagen
st.image("https://www.masterturismo.it/wp-content/uploads/2017/09/logo-eurostars.png", width=80)

import streamlit as st

# Título de la aplicación
st.title("Mi Aplicación en Streamlit")

# Crear una barra lateral con opciones
st.sidebar.title("Opciones")

# Añadir elementos a la barra lateral
opcion_seleccionada = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Opción 1", "Opción 2", "Opción 3"]
)

st.sidebar.write("Puedes usar esta barra para seleccionar opciones adicionales.")

# Mostrando la opción seleccionada en el cuerpo de la aplicación
st.write(f"Has seleccionado: {opcion_seleccionada}")

# Agregar otras opciones en la barra lateral
if st.sidebar.button("Botón de ejemplo"):
    st.write("¡Haz hecho clic en el botón de la barra lateral!")



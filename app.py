import streamlit as st


st.set_page_config(
    page_title="Análisis de rentabilidad de expansión hotelera",  # Título en la pestaña
    page_icon="🏨",  # Ícono en la pestaña, puedes usar emojis o enlaces de imágenes
    layout="wide"  # Configuración de ancho de página, puede ser "centered" o "wide"
)




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
st.title("ৎ୭Análisis de rentabilidad de expansiónৎ୭")
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

#BARRA LATERAL IZQUIERDO MENÚ CON LAS OPCIONES.
#Crear una barra lateral con opciones
st.sidebar.title("_Opciones_")
#Descripción barra lateral.
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        Selecciona una opción de las siguientes para explorar diferentes secciones de la aplicación.
    </div>
    <br><br> <!-- Dos saltos de línea en blanco -->
    """, 
    unsafe_allow_html=True
)

# Añadir un espacio en blanco para separar.
st.markdown("<br>", unsafe_allow_html=True)  # Esto agrega un salto de línea

#Crear opciones en la barra lateral
st.sidebar.button("Opción 1")
st.sidebar.button("Opción 2")
st.sidebar.button("Opción 3")







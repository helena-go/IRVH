import streamlit as st
import time


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

# Centrar el título usando HTML y CSS
st.markdown(
    """
    <h1 style="text-align: center; font-size: 2.5em; font-weight: bold;">
        ৎ୭ Análisis de rentabilidad ৎ୭
    </h1>
    """,
    unsafe_allow_html=True
)

#Subtitulo
st.markdown("<h2 style='text-align: center; font-style: italic; font-size: 18px; '>Eurostars hotel company</h2>", unsafe_allow_html=True)


#IMAGENES:

#Imagen zona superior izquierda
# Insertar la imagen en la parte superior izquierda usando HTML
# Insertar dos imágenes, una más arriba que la otra en la parte superior izquierda usando HTML y CSS
# Primera imagen
st.image("https://www.ecured.cu/images/thumb/e/e5/Logo_usc.svg/320px-Logo_usc.svg.png", width=50)



# Segunda imagen
col1, col2 = st.columns([3, 4])  # El número define el ancho relativo de las columnas (2 es más estrecho que 3)
# Crear un espacio vacío donde la imagen aparecerá después del retardo
placeholder = st.empty()

# Retardo antes de mostrar la imagen (simula una animación de aparición)
time.sleep(2)


# En la primera columna (col1) se coloca la imagen
col1.image("http://www.santiagoturismo.com/files/full/2017/07/GHSantiago026.jpg", caption="Santiago de Compostela", width=400)

# En la segunda columna (col2) se coloca el texto
#Texto a la derecha de la imagen descirbiendo el proyecto.
col2.markdown("""
    <div style="text-align: center;">
    
    _Este proyecto, bajo el título Expansión hotelera basada en datos, presenta como
    principal objetivo desarrollar una buena solución para que el equipo de expansión
    de una cadena hotelera sea capaz de identificar nuevas oportunidades para realizar
    una ampliación de la cadena y tomar decisiones de manera precisa._

    _Debido al enorme crecimiento del sector hotelero, en las grandes compañías
    hoteleras surge la necesidad de realizar una expansión en diferentes ubicaciones
    las cuales deben ser previamente analizadas para asegurar el éxito de la cadena.
    Para poder llevar a cabo esta expansión y que esta sea exitosa, deben de tomarse
    decisiones informadas y fundamentadas para poder asegurar así un crecimiento
    sustentable de la cadena hotelera._
    </div>

""", 
    unsafe_allow_html=True)

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
st.sidebar.button("Predecir IR")
st.sidebar.button("Opción 2")
st.sidebar.button("Opción 3")


# Predecir IR
if opcion == "Predecir IR":
    st.title("Predicción de Índice de Rentabilidad Hotelera")
    exec(open("predecir_ir.py").read())  # Ejecuta el código del archivo predecir_ir.py




import streamlit as st

st.set_page_config(
    page_title="Análisis de Rentabilidad Hotelera",  # Título en la pestaña
    page_icon="🏨",  # Ícono en la pestaña, puedes usar emojis o enlaces de imágenes
    layout="wide"  # Configuración de ancho de página, puede ser "centered" o "wide"
)

#COLOR DE TEXTO Y TÍTULO
# Estilos personalizados usando HTML y CSS
st.markdown(
    """
    <style>
    /* Fondo de la página */
    .main {
        background-color: #f4f4f4; /* Fondo claro y elegante */
        color: #333333; /* Color de fuente sobrio */
        font-family: 'Arial', sans-serif; /* Tipografía parecida a la de Eurostars */
    }
    /* Encabezado principal */
    h1 {
        color: #4A4A4A; /* Color elegante para el título */
        font-size: 2.5em;
        font-family: 'Times New Roman', serif; /* Tipografía clásica para títulos */
        text-align: center;
        margin-top: 20px;
    }
    /* Subtítulo y texto */
    h2, p, .stMarkdown {
        color: #5a5a5a; /* Texto en color gris oscuro */
        font-size: 1.2em;
    }
    /* Caja de Streamlit para dar bordes suaves */
    .stMarkdown {
        background-color: #ffffff; /* Fondo blanco elegante */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    /* Personalización de botones */
    .stButton button {
        background-color: #4A4A4A;
        color: white;
        font-size: 1em;
        border-radius: 4px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown("<h1>🔍 Análisis de Rentabilidad Hotelera 🏨</h1>", unsafe_allow_html=True)

# Subtítulo
st.markdown("<p style='text-align: center; color: #5a5a5a;'>Explora la rentabilidad de diferentes ubicaciones para la expansión hotelera con una interfaz intuitiva y elegante.</p>", unsafe_allow_html=True)

# Ejemplo de contenido con estilos de caja y texto centrado
st.markdown("<div class='stMarkdown'>Aquí se muestra la información sobre las ubicaciones con rentabilidad alta, media y baja, basada en la puntuación de clientes y otros factores.</div>", unsafe_allow_html=True)

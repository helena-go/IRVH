import streamlit as st


st.set_page_config(
    page_title="Análisis de Rentabilidad Hotelera",  # Título en la pestaña
    page_icon="🏨",  # Ícono en la pestaña, puedes usar emojis o enlaces de imágenes
    layout="wide"  # Configuración de ancho de página, puede ser "centered" o "wide"
)



#COLOR DE TEXTO

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #2E86C1;">Análisis de Rentabilidad Hotelera 🏨</h1>
        <p style="font-size:18px; color: #34495E;">Explora la rentabilidad de ubicaciones para la expansión hotelera con visualizaciones interactivas</p>
    </div>
    """,
    unsafe_allow_html=True
)


with st.form("My form"):
    first = st.text_input("First name")
    last = st.text_input("Last name")
    if st.form_submit_button("Submit"):
        st.write(first+" "+last)

css="""
<style>
    [data-testid="stForm"] {
        background: Black;
    }
</style>
"""
st.write(css, unsafe_allow_html=True)

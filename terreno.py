import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Clasificador de Terreno",
    page_icon="🏞️",
    layout="centered"
)

# Estilos CSS para un diseño moderno
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
    }
    .subtitle {
        font-size: 24px;
        color: #4b5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .label {
        font-size: 20px;
        color: #374151;
        margin-bottom: 0.5rem;
    }
    .result {
        font-size: 28px;
        font-weight: bold;
        color: #15803d;
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        background-color: #dcfce7;
        border-radius: 10px;
    }
    .stNumberInput > div > div > input {
        font-size: 18px;
        padding: 0.5rem;
    }
    .stButton > button {
        font-size: 20px;
        background-color: #1e3a8a;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# Función para determinar el tipo de terreno
def determinar_tipo_terreno(p, chp):
    if p < 3:
        if chp < 101:
            return "Terreno Plano"
        elif chp < 500:
            return "Terreno Lomerío"
        else:
            return "Terreno Montañoso"
    elif p >= 5:
        return "Terreno Montañoso"
    else:
        if chp < 500:
            return "Terreno Lomerío"
        else:
            return "Terreno Montañoso"

# Título y descripción
st.markdown('<div class="title">Clasificador de Terreno para Carreteras</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ingresa los valores para determinar el tipo de terreno</div>', unsafe_allow_html=True)

# Entradas del usuario
st.markdown('<div class="label">Pendiente Longitudinal (P) en %</div>', unsafe_allow_html=True)
pendiente = st.number_input("", min_value=0.0, max_value=100.0, value=0.0, step=0.1, label_visibility="collapsed")

st.markdown('<div class="label">Curvatura Horizontal Promedio (CHP) en Grad/km</div>', unsafe_allow_html=True)
chp = st.number_input("", min_value=0.0, max_value=1000.0, value=0.0, step=1.0, label_visibility="collapsed")

# Botón para calcular
if st.button("Calcular Tipo de Terreno"):
    if pendiente >= 0 and chp >= 0:
        tipo_terreno = determinar_tipo_terreno(pendiente, chp)
        st.markdown(f'<div class="result">El tipo de terreno es: {tipo_terreno}</div>', unsafe_allow_html=True)
    else:
        st.error("Por favor, ingresa valores válidos (no negativos).")


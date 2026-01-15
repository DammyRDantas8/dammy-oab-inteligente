import streamlit as st

# 1. Configurações Visuais EXCLUSIVAS deste App
st.set_page_config(page_title="Estudos OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    /* Estilo exclusivo do Hub de Estudos OAB */
    .stApp {
        background-color: #800020; /* Vinho */
    }
    
    h1 {
        color: #FFFFFF !important;
    }

    /* Arial Black 14 para textos menores e labels */
    .stMarkdown, p, label {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
    }

    /* Caixas de Seleção e Radio em AZUL BEBÊ */
    .stSelectbox div[data-baseweb="select"], .stRadio div[role="radiogroup"] {
        background-color: #89CFF0 !important; 
        border-radius: 5px;
        padding: 5px;
    }
    
    /* Texto preto dentro do Azul Bebê */
    .stSelectbox div[data-baseweb="select"] *, .stRadio div[role="radiogroup"] * {
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #4D0013 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Identidade da Estudante
st.title("⚖️ Sistema de Estudos OAB 46")
st.write("Direito | Direito Digital")
st.write("🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python")

# 3. Módulos
menu = st.sidebar.selectbox("Escolha o módulo:", ["Simulado 1ª Fase", "English: Law & Daily"])

if menu == "Simulado 1ª Fase":
    st.header("🎯 Treino para a Prova")
    q = st.radio("Questão de Ética: O advogado pode fazer publicidade paga?", ["A) Sim", "B) Não"])
    if st.button("Validar"):
        st.write("Resultado em análise...")

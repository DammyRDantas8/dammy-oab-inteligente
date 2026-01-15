import streamlit as st

# 1. Configurações de Estilo (Fundo Vinho e Azul Bebê)
st.set_page_config(page_title="Estudos OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO VINHO ESCURO */
    .stApp { background-color: #4D0013 !important; }
    
    /* TÍTULOS E CONFIGURAÇÕES (BRANCO - TAMANHO DE TÍTULO) */
    .texto-branco-titulo {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 24px !important; /* Tamanho de Título */
        line-height: 1.5;
    }

    /* PERGUNTAS E RESPOSTAS (PRETO - ARIAL BLACK 14) */
    .stMarkdown p, .stSubheader, label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
    }

    /* CAIXAS AZUL BEBÊ */
    div[data-baseweb="select"], div[role="radiogroup"] {
        background-color: #89CFF0 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }

    /* BOTÃO DOURADO */
    div.stButton > button {
        background-color: #C5A021 !important;
        color: black !important;
        font-family: 'Arial Black' !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO (Tudo em Branco e Tamanho de Título)
st.markdown("""
    <div class="texto-branco-titulo">
        ⚖️ SISTEMA DE ESTUDOS OAB 46<br>
        DAMIANA RODRIGUES DANTAS<br>
        DIREITO | DIREITO DIGITAL | DEV DE AGENTES IA<br>
        ⚖️ OAB | 🛡️ HARVARD CS50 | 〽️ MICHIGAN PYTHON | 🐍 PYTHON<br>
        <br>
        🎯 TREINO PARA OAB
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# 3. CONTEÚDO DE ESTUDO (Preto - Arial Black 14)
st.sidebar.title("MÓDULO:")
menu = st.sidebar.selectbox("", ["Simulado 1ª Fase"])

if menu == "Simulado 1ª Fase":
    st.markdown('<p class="stMarkdown">QUESTÃO DE ÉTICA PROFISSIONAL:</p>', unsafe_allow_html=True)
    
    q = st.radio("Selecione:", 
                ["A) SIM, É PERMITIDO", "B) NÃO, É VEDADO"], 
                label_visibility="collapsed")
    
    if st.button("VALIDAR"):
        st.write("Processando...")

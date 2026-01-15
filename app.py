import streamlit as st

# 1. Configurações de Estilo (Vinho Bordô Profundo e Fontes Memorizadas)
st.set_page_config(page_title="Simulado OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    .stApp, section[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #2D000B !important;
    }
    section[data-testid="stSidebar"] { border-right: none !important; }

    section[data-testid="stSidebar"] .stMarkdown p, section[data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        font-family: 'Arial', sans-serif !important;
        font-size: 16px !important;
    }

    .texto-branco-titulo {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 24px !important; 
        line-height: 1.5;
    }

    .pergunta-branca {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
        margin-top: 20px;
    }

    div[role="radiogroup"] {
        background-color: #89CFF0 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }

    div[role="radiogroup"] label p {
        color: #000000 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
    }

    div.stButton > button {
        background-color: #C5A021 !important;
        color: black !important;
        font-family: 'Arial Black' !important;
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho (Padrão Memorizado)

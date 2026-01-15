import streamlit as st

# Configurações de Estilo Finais
st.set_page_config(page_title="Estudos OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    /* 1. Unificação do Vinho Escuro em todo o fundo */
    .stApp, section[data-testid="stSidebar"], .main {
        background-color: #4D0013 !important;
    }
    
    /* 2. Título Principal em Branco */
    h1 {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif;
    }

    /* 3. TODO o texto do painel central em PRETO (Arial Black 14) */
    .stMarkdown, p, label, .stSubheader, span, div {
        color: #000000 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
    }

    /* Ajuste para as qualificações no topo continuarem brancas sobre o vinho */
    .stWrite p {
        color: #FFFFFF !important;
    }

    /* 4. Caixas em Azul Bebê com texto interno PRETO */
    .stSelectbox div[data-baseweb="select"], .stRadio div[role="radiogroup"] {
        background-color: #89CFF0 !important; 
        border-radius: 5px;
        padding: 8px;
    }
    
    .stSelectbox div[data-baseweb="select"] *, .stRadio div[role="radiogroup"] * {
        color: #000000 !important;
    }

    /* 5. Botão Dourado */
    div.stButton > button:first-child {
        background-color: #C5A021;
        color: #000000;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Interface do Sistema
st.title("⚖️ Sistema de Estudos OAB 46")
st.markdown(f"*Damiana Rodrigues Dantas*")
st.write("Direito | Direito Digital")
st.write("🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python")

st.sidebar.title("📚 Roteiro OAB")
menu = st.sidebar.selectbox("Escolha o módulo:", ["Simulado 1ª Fase", "English: Law & Daily"])

if menu == "Simulado 1ª Fase":
    st.header("🎯 Treino para a Prova")
    q = st.radio("Questão de Ética: O advogado pode fazer publicidade paga?", ["A) Sim", "B) Não"])
    if st.button("Validar Resposta"):
        st.success("Resposta enviada com sucesso!")

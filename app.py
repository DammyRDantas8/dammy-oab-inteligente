import streamlit as st

# 1. Configurações de Estilo (Cores e Fontes Memorizadas)
st.set_page_config(page_title="Simulado OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO VINHO BORDÔ PROFUNDO UNIFICADO */
    .stApp, section[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #2D000B !important;
    }
    
    /* REMOVE DIVISÓRIAS DA BARRA LATERAL */
    section[data-testid="stSidebar"] { border-right: none !important; }

    /* TEXTO "Módulo" EM BRANCO */
    section[data-testid="stSidebar"] .stMarkdown p, section[data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        font-family: 'Arial', sans-serif !important;
        font-size: 16px !important;
    }

    /* CABEÇALHO (BRANCO - TAMANHO DE TÍTULO) */
    .texto-branco-titulo {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 24px !important; 
        line-height: 1.5;
    }

    /* PERGUNTA EM BRANCO (ARIAL BLACK 14) */
    .pergunta-branca {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
        margin-top: 20px;
    }

    /* CAIXAS DE RESPOSTA EM AZUL BEBÊ COM TEXTO PRETO (ARIAL BLACK 14) */
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

    /* BOTÃO DOURADO */
    div.stButton > button {
        background-color: #C5A021 !important;
        color: black !important;
        font-family: 'Arial Black' !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO (Grafia Normal, Branco, Tamanho de Título)
st.markdown("""
    <div class="texto-branco-titulo">
        ⚖️ Sistema de Estudos OAB 46<br>
        Damiana Rodrigues Dantas<br>
        Direito | Direito Digital | Dev de Agentes IA<br>
        ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python<br>
        <br>
        🎯 Treino para OAB
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# 3. CONTEÚDO DE ESTUDO: DIREITO DO TRABALHO
st.sidebar.markdown("Módulo:")
menu = st.sidebar.selectbox("", ["Direito do Trabalho"], label_visibility="collapsed")

if menu == "Direito do Trabalho":
    st.markdown('<p class="pergunta-branca">Área: Direito do Trabalho</p>', unsafe_allow_html=True)
    st.markdown('<p class="pergunta-branca">Questão: Qual o prazo prescricional para o trabalhador pleitear créditos resultantes das relações de trabalho após a extinção do contrato?</p>', unsafe_allow_html=True)
    
    # Respostas em Preto (Arial Black 14)
    q = st.radio("", 
                ["A) 5 anos, até o limite de 2 anos após a extinção", 
                 "B) 2 anos, independentemente do tempo de contrato",
                 "C) 3 anos para verbas rescisórias"], 
                label_visibility="collapsed")
    
    if st.button("Validar Resposta"):
        if "A)" in q:
            st.success("Correto! Art. 7º, XXIX da Constituição Federal.")
        else:
            st.error("Incorreto. O prazo é de 5 anos para o curso do contrato, limitado a 2 anos após o término.")

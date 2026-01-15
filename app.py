import streamlit as st

# 1. Configurações de Estilo (Fundo Preto Total e Letras Contornadas)
st.set_page_config(page_title="Foco 1ª Fase OAB - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO TOTAL PRETO ABSOLUTO */
    .stApp, section[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] { border-right: none !important; }

    /* EFEITO DE LETRA CONTORNADA (OUTLINE) */
    .letra-contornada {
        font-weight: bold;
        text-shadow: 
            -2px -2px 0 #000,  
             2px -2px 0 #000,
            -2px  2px 0 #000,
             2px  2px 0 #000;
        line-height: 1.5;
    }

    /* CORES DAS LETRAS */
    .cor-branca { color: #FFFFFF !important; }
    .cor-dourada { color: #C5A021 !important; } 
    .cor-azul-cintilante { color: #00FFFF !important; }

    /* FONTES E TAMANHOS */
    .texto-titulo { font-family: 'Arial Black', sans-serif !important; font-size: 24px !important; }
    .pergunta-estudo { font-family: 'Arial Black', sans-serif !important; font-size: 16px !important; margin-top: 20px; }

    /* ÁREA DE RESPOSTAS EM PRETO */
    div[role="radiogroup"] {
        background-color: #000000 !important;
        padding: 10px !important;
    }

    /* OPÇÕES DE RESPOSTA EM DOURADO */
    div[role="radiogroup"] label p {
        color: #C5A021 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
        text-shadow: 2px 2px 0 #000 !important;
    }

    /* BOTÃO DOURADO */
    div.stButton > button {
        background-color: #C5A021 !important;
        color: black !important;
        font-family: 'Arial Black' !important;
        border: 2px solid #000 !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO (Mantido em Branco e Dourado conforme solicitado)
st.markdown("""
    <div class="letra-contornada cor-branca texto-titulo">
        ⚖️ Sistema de Estudos OAB 46<br>
        Damiana Rodrigues Dantas<br>
        <span class="cor-dourada">Direito | Direito Digital | Dev de Agentes IA</span><br>
        ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python<br>
        <br>
        🎯 Treino para OAB - FOCO 1ª FASE
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# 3. MÓDULO DE QUESTÕES
st.sidebar.markdown('<p class="letra-contornada cor-branca" style="font-family:Arial; font-size:16px;">Módulo:</p>', unsafe_allow_html=True)
menu = st.sidebar.selectbox("", ["Questões Objetivas"], label_visibility="collapsed")

if menu == "Questões Objetivas":
    # ÁREA e QUESTÃO em AZUL CINTILANTE | RESPOSTAS em DOURADO
    st.markdown('<p class="letra-contornada pergunta-estudo"><span class="cor-azul-cintilante">Área:</span> <span class="cor-dourada">Direito do Trabalho (1ª Fase)</span></p>', unsafe_allow_html=True)
    
    st.markdown("""
        <p class="letra-contornada pergunta-estudo">
            <span class="cor-azul-cintilante">Questão:</span> 
            <span class="cor-dourada">O empregado que é dispensado sem justa causa tem direito ao saque do FGTS e à indenização compensatória de:</span>
        </p>
    """, unsafe_allow_html=True)
    
    q = st.radio("", 
                ["A) 20% sobre os depósitos", 
                 "B) 40% sobre os depósitos",
                 "C) 50% sobre os depósitos"], 
                label_visibility="collapsed")
    
    if st.button("Validar Resposta"):
        if "B)" in q:
            st.success("Correto! Art. 18, § 1º da Lei 8.036/90. A multa é de 40% em caso de dispensa sem justa causa.")
        else:
            st.error("Incorreto. A multa rescisória devida pelo empregador é de 40% sobre o saldo do FGTS.")

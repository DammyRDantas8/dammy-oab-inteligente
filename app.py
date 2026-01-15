import streamlit as st

# 1. Configurações de Estilo (Fundo Preto Absoluto e Letras Contornadas)
st.set_page_config(page_title="Foco 1ª Fase OAB - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO TOTAL PRETO (Principal e Sidebar) */
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

    /* FONTES E TAMANHOS */
    .texto-titulo { font-family: 'Arial Black', sans-serif !important; font-size: 24px !important; }
    .pergunta-estudo { font-family: 'Arial Black', sans-serif !important; font-size: 16px !important; margin-top: 20px; }

    /* CAIXAS DE RESPOSTA (Azul Bebê com Texto Preto Arial Black 14) */
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
        border: 2px solid #000 !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO (Padrão Memorizado com Letras Contornadas)
st.markdown("""
    <div class="letra-contornada cor-branca texto-titulo">
        ⚖️ Sistema de Estudos OAB 46<br>
        Damiana Rodrigues Dantas<br>
        Direito | Direito Digital | Dev de Agentes IA<br>
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
    st.markdown('<p class="letra-contornada pergunta-estudo"><span class="cor-dourada">Área:</span> <span class="cor-branca">Direito do Trabalho (1ª Fase)</span></p>', unsafe_allow_html=True)
    
    st.markdown("""
        <p class="letra-contornada pergunta-estudo">
            <span class="cor-dourada">Questão:</span> 
            <span class="cor-branca">Considere que um empregado trabalha em regime de tempo parcial. Após a Reforma Trabalhista, qual a duração máxima semanal permitida para esse regime sem horas suplementares?</span>
        </p>
    """, unsafe_allow_html=True)
    
    q = st.radio("", 
                ["A) 25 horas semanais", 
                 "B) 30 horas semanais",
                 "C) 32 horas semanais"], 
                label_visibility="collapsed")
    
    if st.button("Validar Resposta"):
        if "B)" in q:
            st.success("Correto! Art. 58-A da CLT. O regime de tempo parcial pode ser de até 30 horas semanais (sem horas extras) ou 26 horas (com até 6 horas extras).")
        else:
            st.error("Incorreto. A Reforma de 2017 ampliou o limite para 30 horas semanais sem horas suplementares.")

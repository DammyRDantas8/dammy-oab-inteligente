import streamlit as st

# 1. Configurações de Estilo (Fundo Preto, Azul Cintilante e Dourado)
st.set_page_config(page_title="Foco 1ª Fase OAB - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO TOTAL PRETO */
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
    .cor-azul-cintilante { color: #00FFFF !important; } /* Azul Cintilante / Cyan */

    /* FONTES E TAMANHOS */
    .texto-titulo { font-family: 'Arial Black', sans-serif !important; font-size: 24px !important; }
    .pergunta-estudo { font-family: 'Arial Black', sans-serif !important; font-size: 16px !important; margin-top: 20px; }

    /* CAIXAS DE RESPOSTA (Azul Bebê com Texto DOURADO Arial Black 14) */
    div[role="radiogroup"] {
        background-color: #89CFF0 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }

    div[role="radiogroup"] label p {
        color: #C5A021 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
        text-shadow: 1px 1px 0 #000 !important;
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

# 2. CABEÇALHO (Padrão Memorizado)
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
    # DESTAQUE: 'Área' e 'Questão' em AZUL CINTILANTE | Conteúdo em DOURADO
    st.markdown('<p class="letra-contornada pergunta-estudo"><span class="cor-azul-cintilante">Área:</span> <span class="cor-dourada">Direito do Trabalho (1ª Fase)</span></p>', unsafe_allow_html=True)
    
    st.markdown("""
        <p class="letra-contornada pergunta-estudo">
            <span class="cor-azul-cintilante">Questão:</span> 
            <span class="cor-dourada">O empregado que exerce cargo de gestão, como um gerente de agência bancária com amplos poderes de mando, está sujeito ao controle de jornada?</span>
        </p>
    """, unsafe_allow_html=True)
    
    q = st.radio("", 
                ["A) Sim, deve receber horas extras excedentes à 8ª diária", 
                 "B) Não, pois está excluído do regime de jornada da CLT",
                 "C) Apenas se houver acordo escrito para pagamento de horas extras"], 
                label_visibility="collapsed")
    
    if st.button("Validar Resposta"):
        if "B)" in q:
            st.success("Correto! Art. 62, II da CLT. Os gerentes, assim considerados os exercentes de cargos de gestão, não estão sujeitos ao controle de jornada.")
        else:
            st.error("Incorreto. Cargos de confiança/gestão são exceção ao controle de jornada (Art. 62, II).")

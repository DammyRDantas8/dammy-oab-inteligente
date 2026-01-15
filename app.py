import streamlit as st

# 1. Configurações de Estilo (Fundo Azul Marinho e Letras Contornadas)
st.set_page_config(page_title="Simulado OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO AZUL MARINHO PROFUNDO */
    .stApp, section[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #001F3F !important;
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

    /* CORES ESPECÍFICAS */
    .cor-branca { color: #FFFFFF !important; }
    .cor-dourada { color: #C5A021 !important; } /* Cor do nome 'Questão' e 'Área' */

    /* FONTES */
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

# 2. CABEÇALHO (Letras Brancas com Contorno)
st.markdown("""
    <div class="letra-contornada cor-branca texto-titulo">
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
st.sidebar.markdown('<p class="letra-contornada cor-branca" style="font-family:Arial; font-size:16px;">Módulo:</p>', unsafe_allow_html=True)
menu = st.sidebar.selectbox("", ["Direito do Trabalho"], label_visibility="collapsed")

if menu == "Direito do Trabalho":
    # DESTAQUE: 'Área' e 'Questão' em DOURADO | Conteúdo em BRANCO
    st.markdown('<p class="letra-contornada pergunta-estudo"><span class="cor-dourada">Área:</span> <span class="cor-branca">Direito do Trabalho</span></p>', unsafe_allow_html=True)
    
    st.markdown("""
        <p class="letra-contornada pergunta-estudo">
            <span class="cor-dourada">Questão:</span> 
            <span class="cor-branca">Sobre o intervalo intrajornada, após a Reforma Trabalhista, é correto afirmar que a não concessão ou concessão parcial implica o pagamento:</span>
        </p>
    """, unsafe_allow_html=True)
    
    q = st.radio("", 
                ["A) Da integralidade do período de 1 hora, com natureza salarial", 
                 "B) Apenas do período suprimido, com acréscimo de 50% e natureza indenizatória",
                 "C) Apenas do período suprimido, com natureza salarial"], 
                label_visibility="collapsed")
    
    if st.button("Validar Resposta"):
        if "B)" in q:
            st.success("Correto! Art. 71, § 4º da CLT. A natureza agora é indenizatória e paga-se apenas o tempo suprimido.")
        else:
            st.error("Incorreto. A Reforma de 2017 mudou para natureza indenizatória e apenas sobre o tempo que faltou.")

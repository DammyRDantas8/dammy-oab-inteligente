import streamlit as st

# 1. Configurações de Estilo (Vinho Escuro, Azul Bebê e Fontes)
st.set_page_config(page_title="Estudos OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    /* Fundo Vinho Escuro */
    .stApp, section[data-testid="stSidebar"] {
        background-color: #4D0013 !important;
    }
    
    /* NOME E TÍTULOS DO TOPO (Brancos e Maiores) */
    .titulo-topo {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 24px !important; 
        font-weight: bold;
        line-height: 1.2;
        margin-bottom: 5px;
    }
    
    .subtitulo-topo {
        color: #FFFFFF !important;
        font-family: 'Arial', sans-serif !important;
        font-size: 18px !important;
        line-height: 1.6;
    }

    /* SÍMBOLOS (Cores originais e tamanho equilibrado) */
    .icon {
        font-size: 24px !important;
        vertical-align: middle;
        margin-right: 5px;
    }

    /* PERGUNTAS E RESPOSTAS (Arial Black 14 - PRETO) */
    .stMarkdown p, .stSubheader, label, .stRadio p, .stSelectbox label {
        color: #000000 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
    }

    /* Caixas de Pergunta em Azul Bebê */
    .stSelectbox div[data-baseweb="select"], .stRadio div[role="radiogroup"] {
        background-color: #89CFF0 !important; 
        border-radius: 5px;
        padding: 10px;
    }
    
    .stSelectbox div[data-baseweb="select"] *, .stRadio div[role="radiogroup"] * {
        color: #000000 !important;
    }

    /* Botão Dourado */
    div.stButton > button:first-child {
        background-color: #C5A021;
        color: #000000;
        font-family: 'Arial Black';
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho com Nome e Qualificações (Branco e Maior)
st.markdown(f"""
    <div class="titulo-topo">⚖️ Sistema de Estudos OAB 46</div>
    <div class="subtitulo-topo">
        <b>Damiana Rodrigues Dantas</b><br>
        Direito | Direito Digital | <b>Dev de Agentes IA</b><br>
        <span class="icon">⚖️</span> OAB | 
        <span class="icon">🛡️</span> Harvard CS50 | 
        <span class="icon">〽️</span> Michigan Python | 
        <span class="icon">🐍</span> Python
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# 3. Menu Lateral e Conteúdo
st.sidebar.title("📚 Roteiro OAB")
menu = st.sidebar.selectbox("Escolha o módulo:", ["Simulado 1ª Fase", "English Practice"])

if menu == "Simulado 1ª Fase":
    st.header("🎯 Treino para a Prova")
    st.subheader("Questão de Ética Profissional:")
    
    q = st.radio("O advogado pode exercer a profissão sem estar inscrito na OAB?", 
                ["A) Sim, se tiver o diploma", "B) Não, a inscrição é obrigatória"])
    
    if st.button("Validar Resposta"):
        if q.startswith("B"):
            st.success("Correto! Art. 3º do Estatuto da OAB.")
        else:
            st.error("Incorreto. A inscrição é indispensável.")

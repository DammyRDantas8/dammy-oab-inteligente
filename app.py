import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Estudos OAB 46 - Damiana", layout="wide")

# CSS FORÇADO (Garante as cores Branca no topo e Preta nas perguntas)
st.markdown("""
    <style>
    /* 1. FUNDO VINHO ESCURO */
    .stApp, section[data-testid="stSidebar"], .main {
        background-color: #4D0013 !important;
    }
    
    /* 2. TÍTULOS E QUALIFICAÇÕES (FORÇAR BRANCO E GRANDE) */
    .topo-branco {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        text-align: left;
    }
    .nome-grande { font-size: 32px !important; margin-bottom: 0px; }
    .info-branca { font-size: 18px !important; font-family: 'Arial', sans-serif !important; }

    /* 3. PERGUNTAS E RESPOSTAS (FORÇAR PRETO EM ARIAL BLACK 14) */
    .stMarkdown p, .stSubheader, label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
    }

    /* 4. CAIXAS AZUL BEBÊ */
    div[data-baseweb="select"], div[role="radiogroup"] {
        background-color: #89CFF0 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }

    /* Garante texto preto dentro das caixas */
    div[data-baseweb="select"] *, div[role="radiogroup"] * {
        color: #000000 !important;
    }

    /* 5. BOTÃO DOURADO */
    div.stButton > button {
        background-color: #C5A021 !important;
        color: #000000 !important;
        font-family: 'Arial Black' !important;
    }
    </style>
    """, unsafe_allow_html=True)

# CABEÇALHO (Usando HTML para garantir a cor branca)
st.markdown('<h1 class="topo-branco">⚖️ Sistema de Estudos OAB 46</h1>', unsafe_allow_html=True)
st.markdown(f"""
    <div class="topo-branco">
        <p class="nome-grande"><b>Damiana Rodrigues Dantas</b></p>
        <p class="info-branca">Direito | Direito Digital | <b>Dev de Agentes IA</b></p>
        <p class="info-branca">
            <span style="font-size:24px">⚖️</span> OAB | 
            <span style="font-size:24px">🛡️</span> Harvard CS50 | 
            <span style="font-size:24px">〽️</span> Michigan Python | 
            <span style="font-size:24px">🐍</span> Python
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# INTERFACE DE ESTUDO
st.sidebar.title("📚 Roteiro OAB")
menu = st.sidebar.selectbox("Escolha o módulo:", ["Simulado 1ª Fase", "English Practice"])

if menu == "Simulado 1ª Fase":
    st.header("🎯 Treino para a Prova")
    st.subheader("Questão de Ética Profissional:")
    
    q = st.radio("O advogado pode exercer a profissão sem estar inscrito na OAB?", 
                ["A) Sim, se tiver o diploma", "B) Não, a inscrição é obrigatória"])
    
    if st.button("Validar Resposta"):
        if q.startswith("B"):
            st.success("Correto!")
        else:
            st.error("Incorreto.")

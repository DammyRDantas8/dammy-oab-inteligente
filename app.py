import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Sistema de Estudos OAB 46", layout="wide")

# 2. CSS Corrigido: Texto e Símbolos Sólidos | Neon apenas no Azul
st.markdown("""
    <style>
    /* Fundo Totalmente Preto Absoluto */
    .stApp, [data-testid="stSidebar"], .main {
        background-color: #000000 !important;
    }
    
    /* TEXTOS SÓLIDOS (Branco e Amarelo sem neon) */
    .nome-usuario {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }

    .titulo-sistema, .subtitulo-especialidade, .enunciado-dourado, .feedback-final {
        color: #FFD700 !important;
        font-weight: bold !important;
    }

    /* AZUL FLUORESCENTE ESCURO (Matéria e Botões) */
    .descricao-materia {
        color: #005fcc !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px #007FFF;
    }

    /* Opções de Resposta (Amarelo Sólido e Grande) */
    div[data-testid="stWidgetLabel"] p, label[data-baseweb="radio"] div {
        color: #FFD700 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
    }

    /* BOTÕES: Fundo Preto com Borda e Texto Azul Neon */
    div.stButton > button {
        background-color: #000000 !important;
        color: #005fcc !important;
        border: 2px solid #005fcc !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        height: 3em !important;
        width: 100% !important;
        box-shadow: 0 0 8px #005fcc;
    }
    
    div.stButton > button:hover {
        background-color: #000811 !important;
        box-shadow: 0 0 15px #007FFF;
    }

    hr { border: 0.5px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Símbolos e Textos Sólidos)
st.markdown('<div class="titulo-sistema" style="font-size: 32px;">⚖️ Sistema de Estudos OAB 46</div>', unsafe_allow_html=True)
st.markdown('<div class="nome-usuario" style="font-size: 28px;">Damiana Rodrigues Dantas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo-especialidade" style="font-size: 20px;">Direito | Direito Digital | Dev de Agentes IA</div>', unsafe_allow_html=True)

st.markdown("""
<div style="color: #FFFFFF; font-size: 18px; font-weight: bold;">
    ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. Área da Pergunta
st.markdown('<div style="color: white; font-size: 24px; font-weight: bold;">🎯 Treino para OAB - FOCO 1ª FASE</div>', unsafe_allow_html=True)
st.markdown('<div class="descricao-materia">Esta questão é sobre: Direito do Trabalho (1ª Fase)</div>', unsafe_allow_html=True)

st.markdown('<div class="enunciado-dourado" style="font-size: 22px; margin-bottom: 20px;">Questão: O empregado que é dispensado sem justa causa tem direito ao saque do FGTS e à indenização compensatória de:</div>', unsafe_allow_html=True)

# 5. Opções
alternativas = ["A) 20% sobre os depósitos", "B) 40% sobre os depósitos", "C) 50% sobre os depósitos"]
escolha = st.radio("", alternativas, label_visibility="collapsed")

# 6. Botões
col1, col2 = st.columns(2)

with col1:
    if st.button("Validar Resposta"):
        if "B)" in escolha:
            st.markdown('<div class="feedback-final" style="font-size: 24px; margin-top:15px;">✅ Resposta Correta!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="feedback-final" style="font-size: 24px; margin-top:15px;">❌ Incorreta. A resposta certa é a B.</div>', unsafe_allow_html=True)

with col2:
    if st.button("Próxima Questão"):
        st.rerun()

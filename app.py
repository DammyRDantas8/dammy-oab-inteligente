[21:03, 15/01/2026] Dammy R Dantas: import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Sistema de Estudos OAB 46", layout="wide")

# 2. CSS focado apenas nas mudanças solicitadas
st.markdown("""
    <style>
    /* Fundo Totalmente Preto */
    .stApp, [data-testid="stSidebar"], .main {
        background-color: #000000 !important;
    }
    
    /* Cabeçalho Identidade Visual */
    .titulo-sistema { color: #FFD700; font-size: 32px !important; font-weight: bold; }
    .nome-usuario { color: white; font-size: 28px !important; font-weight: bold; }
    .subtitulo-especialidade { color: #FFD700; font-size: 20px !important; }

    /* Texto das Opções (A, B, C) - Dourado Vibrante */
    div[data-testid="stWidgetLabel"] p, label[data-baseweb="radio"] div {
        color: #FFD700 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
    }

    /* AZUL FLUORESCENTE para a descrição da matéria */
    .descricao-materia {
        color: #007FFF !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        text-shadow: 0 0 8px #007FFF;
    }

    /* BOTÕES: Fundo Preto, Borda e Texto Azul Fluorescente */
    div.stButton > button {
        background-color: #000000 !important;
        color: #007FFF !important;
        border: 2px solid #007FFF !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        height: 3em !important;
        width: 100% !important;
        box-shadow: 0 0 5px #007FFF;
    }

    .feedback-final {
        color: #FFD700 !important;
        font-size: 24px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho
st.markdown('<div class="titulo-sistema">⚖️ Sistema de Estudos OAB 46</div>', unsafe_allow_html=True)
st.markdown('<div class="nome-usuario">Damiana Rodrigues Dantas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo-especialidade">Direito | Direito Digital | Dev de Agentes IA</div>', unsafe_allow_html=True)

st.divider()

# 4. Questão e Matéria
st.markdown('<div style="color: white; font-size: 24px; font-weight: bold;">🎯 Treino para OAB - FOCO 1ª FASE</div>', unsafe_allow_html=True)
st.markdown('<div class="descricao-materia">Esta questão é sobre: Direito do Trabalho (1ª Fase)</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #FFD700; font-size: 22px; font-weight: bold; margin-bottom: 20px;">Questão: O empregado que é dispensado sem justa causa tem direito ao saque do FGTS e à indenização compensatória de:</div>', unsafe_allow_html=True)

alternativas = ["A) 20% sobre os depósitos", "B) 40% sobre os depósitos", "C) 50% sobre os depósitos"]
escolha = st.radio("", alternativas, label_visibility="collapsed")

# 5. Botões Validar e Próxima Questão
col1, col2 = st.columns(2)

with col1:
    if st.button("Validar Resposta"):
        if "B)" in escolha:
            st.markdown('<div class="feedback-final">✅ Resposta Correta!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="feedback-final">❌ Incorreta. Tente novamente.</div>', unsafe_allow_html=True)

with col2:
    if st.button("Próxima Questão"):
        st.rerun()
[21:07, 15/01/2026] Dammy R Dantas: HHHJJJJ
import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Sistema de Estudos OAB 46", layout="wide")

# 2. CSS com Efeito Fluorescente (Neon) em todas as cores
st.markdown("""
    <style>
    /* Fundo Totalmente Preto Absoluto */
    .stApp, [data-testid="stSidebar"], .main {
        background-color: #000000 !important;
    }
    
    /* BRANCO FLUORESCENTE */
    .nome-usuario, .certificacoes-texto {
        color: #FFFFFF !important;
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #FFFFFF;
        font-weight: bold !important;
    }

    /* AMARELO/DOURADO FLUORESCENTE */
    .titulo-sistema, .subtitulo-especialidade, .enunciado-dourado, .feedback-final {
        color: #FFD700 !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700;
    }

    /* AZUL FLUORESCENTE */
    .descricao-materia {
        color: #007FFF !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px #007FFF, 0 0 20px #007FFF;
    }

    /* Estilo das Opções (A, B, C) - Dourado Fluorescente e Grande */
    div[data-testid="stWidgetLabel"] p, label[data-baseweb="radio"] div {
        color: #FFD700 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        text-shadow: 0 0 5px #FFD700;
    }

    /* BOTÕES: Fundo Preto, Borda e Texto Azul Fluorescente */
    div.stButton > button {
        background-color: #000000 !important;
        color: #007FFF !important;
        border: 2px solid #007FFF !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        height: 3em !important;
        width: 100% !important;
        box-shadow: 0 0 10px #007FFF;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #001a33 !important;
        box-shadow: 0 0 20px #007FFF;
    }

    hr { border: 0.5px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho Restaurado com Símbolos e Efeito Neon
st.markdown('<div class="titulo-sistema" style="font-size: 32px;">⚖️ Sistema de Estudos OAB 46</div>', unsafe_allow_html=True)
st.markdown('<div class="nome-usuario" style="font-size: 28px;">Damiana Rodrigues Dantas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo-especialidade" style="font-size: 20px;">Direito | Direito Digital | Dev de Agentes IA</div>', unsafe_allow_html=True)

# Linha de certificações com todos os ícones originais
st.markdown("""
<div class="certificacoes-texto" style="font-size: 18px;">
    ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. Área da Pergunta
st.markdown('<div style="color: white; font-size: 24px; font-weight: bold; text-shadow: 0 0 5px white;">🎯 Treino para OAB - FOCO 1ª FASE</div>', unsafe_allow_html=True)
st.markdown('<div class="descricao-materia">Esta questão é sobre: Direito do Trabalho (1ª Fase)</div>', unsafe_allow_html=True)

st.markdown('<div class="enunciado-dourado" style="font-size: 22px; margin-bottom: 20px;">Questão: O empregado que é dispensado sem justa causa tem direito ao saque do FGTS e à indenização compensatória de:</div>', unsafe_allow_html=True)

# 5. Opções de Marcar
alternativas = ["A) 20% sobre os depósitos", "B) 40% sobre os depósitos", "C) 50% sobre os depósitos"]
escolha = st.radio("", alternativas, label_visibility="collapsed")

# 6. Botões lado a lado
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

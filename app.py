import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Sistema de Estudos OAB 46", layout="wide")

# 2. CSS para fundo PRETO ABSOLUTO e letras DOURADAS
st.markdown("""
    <style>
    /* Fundo Totalmente Preto (Pure Black) */
    .stApp, [data-testid="stSidebar"], .main, [data-testid="stHeader"] {
        background-color: #000000 !important;
    }
    
    /* Cabeçalho Identidade Visual */
    .titulo-sistema { color: #FFD700; font-size: 32px !important; font-weight: bold; }
    .nome-usuario { color: white; font-size: 28px !important; font-weight: bold; }
    .subtitulo-especialidade { color: #FFD700; font-size: 20px !important; }
    .certificacoes { color: white; font-size: 18px !important; }

    /* Estilo do Enunciado e Informação da Matéria */
    .treino-foco { color: white; font-size: 24px !important; font-weight: bold; margin-top: 20px; }
    .descricao-materia { color: #00BFFF; font-size: 20px !important; font-weight: bold; }
    .enunciado-dourado { color: #FFD700; font-size: 22px !important; font-weight: bold; margin-bottom: 25px; }

    /* VISIBILIDADE DAS OPÇÕES: Dourado Vibrante, Sem Transparência */
    div[data-testid="stWidgetLabel"] p, label[data-baseweb="radio"] div {
        color: #FFD700 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        opacity: 1 !important;
    }

    /* Feedback da Resposta (Amarelo Dourado) */
    .feedback-final {
        color: #FFD700 !important;
        font-size: 24px !important;
        font-weight: bold;
        margin-top: 20px;
    }
    
    /* Ajuste para a Sidebar não ficar com divisórias cinzas */
    [data-testid="stSidebar"] {
        border-right: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Damiana Rodrigues Dantas)
st.markdown('<div class="titulo-sistema">⚖️ Sistema de Estudos OAB 46</div>', unsafe_allow_html=True)
st.markdown('<div class="nome-usuario">Damiana Rodrigues Dantas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo-especialidade">Direito | Direito Digital | Dev de Agentes IA</div>', unsafe_allow_html=True)
st.markdown('<div class="certificacoes">⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python</div>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)

# 4. Área da Pergunta
st.markdown('<div class="treino-foco">🎯 Treino para OAB - FOCO 1ª FASE</div>', unsafe_allow_html=True)
st.markdown('<div class="descricao-materia">Esta questão é sobre: Direito do Trabalho (1ª Fase)</div>', unsafe_allow_html=True)

st.markdown('<div class="enunciado-dourado">Questão: O empregado que é dispensado sem justa causa tem direito ao saque do FGTS e à indenização compensatória de:</div>', unsafe_allow_html=True)

# 5. Opções com letras douradas grandes
alternativas = ["A) 20% sobre os depósitos", "B) 40% sobre os depósitos", "C) 50% sobre os depósitos"]
escolha = st.radio("", alternativas, label_visibility="collapsed")

# Placeholder para o resultado
resultado_placeholder = st.empty()

if st.button("Validar Resposta"):
    if "B)" in escolha:
        resultado_placeholder.markdown('<div class="feedback-final">✅ Resposta Correta! A indenização é de 40%.</div>', unsafe_allow_html=True)
    else:
        resultado_placeholder.markdown('<div class="feedback-final">❌ Resposta Incorreta. A alternativa correta é a B.</div>', unsafe_allow_html=True)

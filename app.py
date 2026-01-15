import streamlit as st
import json
import random

# ==========================================
# 1. MOTOR DE INTELIGÊNCIA DO AGENTE (DATA MINING)
# ==========================================
def motor_agente_ia():
    """
    Simula o agente que conhece as recorrências da FGV (2021-2026)
    e as atualizações legislativas mais recentes.
    """
    banco_estratégico = [
        {
            "area": "Ética (Recorrência: 100%)",
            "pergunta": "Sobre as prerrogativas do advogado, em caso de prisão em flagrante por motivo ligado ao exercício da profissão, é indispensável:",
            "opcoes": [
                "A) A presença de um representante da OAB para lavratura do auto",
                "B) Apenas a comunicação posterior à seccional da OAB",
                "C) O acompanhamento de um juiz corregedor"
            ],
            "correta": "A)",
            "explica": "Art. 7, § 3º do Estatuto. É direito do advogado a presença de representante da OAB sob pena de nulidade."
        },
        {
            "area": "Trabalho (Recorrência: Alta)",
            "pergunta": "No teletrabalho, a alteração do regime presencial para o remoto requer:",
            "opcoes": [
                "A) Mútuo acordo e aditivo contratual escrito",
                "B) Determinação unilateral do empregador com aviso de 48h",
                "C) Apenas concordância verbal das partes"
            ],
            "correta": "A)",
            "explica": "Art. 75-C, § 1º da CLT. Requer mútuo acordo e registro escrito."
        },
        {
            "area": "Ética (Tendência 2026)",
            "pergunta": "O uso de inteligência artificial generativa para a redação de peças processuais pelo advogado é:",
            "opcoes": [
                "A) Vedado pelo Tribunal de Ética",
                "B) Permitido, desde que haja supervisão e responsabilidade técnica do profissional",
                "C) Obrigatório para agilizar a prestação jurisdicional"
            ],
            "correta": "B)",
            "explica": "A tecnologia é ferramenta meio; a responsabilidade final pelo conteúdo é sempre do advogado inscrito."
        }
    ]
    return banco_estratégico

# ==========================================
# 2. CONFIGURAÇÕES VISUAIS (PADRÃO DAMIANA)
# ==========================================
st.set_page_config(page_title="IA-Powered OAB - Damiana", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    .letra-contornada {
        font-weight: bold;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
        line-height: 1.5;
    }
    .cor-branca { color: #FFFFFF !important; }
    .cor-dourada { color: #C5A021 !important; } 
    .cor-azul-cintilante { color: #00FFFF !important; }
    .texto-titulo { font-family: 'Arial Black'; font-size: 26px; }
    
    /* REMOÇÃO DE FUNDOS E AJUSTE DE CORES */
    div[role="radiogroup"] { background-color: #000000 !important; }
    div[role="radiogroup"] label p { 
        color: #C5A021 !important; 
        font-family: 'Arial Black' !important; 
        font-size: 16px !important;
        text-shadow: 2px 2px 0 #000 !important;
    }
    div.stButton > button {
        background-color: #C5A021; color: black; font-weight: bold; width: 100%; border: 2px solid #000;
    }
    div[data-testid="stNotification"], .stAlert {
        background-color: #000000 !important; border: 1px solid #C5A021 !important;
    }
    div[data-testid="stNotification"] p { color: #FFFFFF !important; font-family: 'Arial Black' !important; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. LÓGICA DE EXECUÇÃO
# ==========================================
if 'banco_de_dados' not in st.session_state:
    st.session_state.banco_de_dados = motor_agente_ia()
    st.session_state.indice = 0
    st.session_state.feedback = None

# Cabeçalho Fixo
st.markdown(f"""
    <div class="letra-contornada cor-branca texto-titulo">
        ⚖️ Sistema Unificado de IA - OAB 46<br>
        Damiana Rodrigues Dantas<br>
        <span class="cor-dourada">Direito | Dev de Agentes IA</span>
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# Questão Atual
banco = st.session_state.banco_de_dados
q = banco[st.session_state.indice]

st.markdown(f'<p class="letra-contornada"><span class="cor-azul-cintilante">Área Recorrente:</span> <span class="cor-dourada">{q["area"]}</span></p>', unsafe_allow_html=True)
st.markdown(f'<p class="letra-contornada"><span class="cor-azul-cintilante">Questão Hiperatualizada:</span> <span class="cor-dourada">{q["pergunta"]}</span></p>', unsafe_allow_html=True)

escolha = st.radio("", q["opcoes"], key=f"quest_{st.session_state.indice}", label_visibility="collapsed")

col1, col2 = st.columns(2)
with col1:
    if st.button("Validar Resposta"):
        if q["correta"] in escolha:
            st.session_state.feedback = f"✅ CORRETO! {q['explica']}"
        else:
            st.session_state.feedback = f"❌ INCORRETO. {q['explica']}"

with col2:
    if st.button("Próxima Questão (IA)"):
        st.session_state.indice = (st.session_state.indice + 1) % len(banco)
        st.session_state.feedback = None
        st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)

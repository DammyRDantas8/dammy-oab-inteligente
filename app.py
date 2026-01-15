import streamlit as st
import json

# 1. CONFIGURAÇÕES VISUAIS (PADRÃO DAMIANA COM SÍMBOLOS)
st.set_page_config(page_title="Simulado 100 Questões OAB - Damiana", layout="wide")

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

# 2. BANCO DE DADOS (EXEMPLO DAS TOP MATÉRIAS - EXPANSÍVEL ATÉ 100)
def carregar_banco_100():
    return [
        {"area": "⚖️ Ética (Peso 1)", "pergunta": "O advogado pode recusar o patrocínio de causa contrária à sua consciência?", "opcoes": ["A) ✅ Sim, é um direito de liberdade profissional", "B) ❌ Não, é obrigado a aceitar se for nomeado"], "correta": "A)", "explica": "Art. 4º do Código de Ética e Disciplina."},
        {"area": "💼 Trabalho (Peso 1)", "pergunta": "A reforma trabalhista limitou o tempo de 'itinerere'?", "opcoes": ["A) ✅ Sim, o tempo de trajeto não é mais tempo à disposição", "B) ❌ Não, continua sendo pago"], "correta": "A)", "explica": "Art. 58, § 2º da CLT."},
        {"area": "🛡️ Constitucional (Peso 1)", "pergunta": "Quem pode propor Ação Direta de Inconstitucionalidade?", "opcoes": ["A) 📜 Qualquer cidadão", "B) 🏛️ O Presidente da República, Mesas da Câmara e Senado, entre outros"], "correta": "B)", "explica": "Art. 103 da CF/88."},
        # [Aqui você deve continuar adicionando as outras 97 questões no mesmo formato]
    ]

# 3. LÓGICA DE ESTADO
if 'banco' not in st.session_state:
    st.session_state.banco = carregar_banco_100()
    st.session_state.indice = 0
    st.session_state.feedback = None

# 4. CABEÇALHO DAMIANA
st.markdown(f"""
    <div class="letra-contornada cor-branca texto-titulo">
        ⚖️ Sistema de Estudos OAB 46 - 100 Questões<br>
        Damiana Rodrigues Dantas<br>
        <span class="cor-dourada">Direito | Direito Digital | Dev de Agentes IA</span><br>
        ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# 5. INTERFACE
q = st.session_state.banco[st.session_state.indice]
st.markdown(f'<p class="letra-contornada"><span class="cor-azul-cintilante">🎯 Matéria:</span> <span class="cor-dourada">{q["area"]}</span></p>', unsafe_allow_html=True)
st.markdown(f'<p class="letra-contornada"><span class="cor-azul-cintilante">📝 Questão {st.session_state.indice + 1}/100:</span> <span class="cor-dourada">{q["pergunta"]}</span></p>', unsafe_allow_html=True)

escolha = st.radio("", q["opcoes"], key=f"q{st.session_state.indice}", label_visibility="collapsed")

c1, c2 = st.columns(2)
with c1:
    if st.button("✅ Validar"):
        if q["correta"] in escolha:
            st.session_state.feedback = f"CORRETO! {q['explica']}"
        else:
            st.session_state.feedback = f"INCORRETO. {q['explica']}"

with c2:
    if st.button("➡️ Próxima"):
        st.session_state.indice = (st.session_state.indice + 1) % len(st.session_state.banco)
        st.session_state.feedback = None
        st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)

import streamlit as st
import json
import os

# 1. CONFIGURAÇÕES VISUAIS (PADRÃO DAMIANA)
st.set_page_config(page_title="IA OAB 46 - Damiana", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    .letra-contornada { font-weight: bold; text-shadow: 2px 2px 0 #000, -2px 2px 0 #000, 2px -2px 0 #000, -2px -2px 0 #000; }
    .cor-branca { color: #FFFFFF !important; }
    .cor-dourada { color: #C5A021 !important; }
    .cor-azul { color: #00FFFF !important; }
    div[role="radiogroup"] label p { color: #C5A021 !important; font-family: 'Arial Black'; font-size: 16px; }
    div.stButton > button { background-color: #C5A021; color: black; font-weight: bold; width: 100%; border: 2px solid #000; }
    div[data-testid="stNotification"] p { color: #FFFFFF !important; font-family: 'Arial Black'; font-size: 18px; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 2. FUNÇÃO QUE LÊ AS QUESTÕES DO ARQUIVO EXTERNO
def carregar_dados():
    if os.path.exists('questoes.json'):
        with open('questoes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    # Se o arquivo não existir, mostra este aviso
    return [{"area": "⚠️ Atenção", "pergunta": "O arquivo 'questoes.json' ainda não foi criado no GitHub.", "opcoes": ["A", "B"], "correta": "A", "explica": ""}]

if 'banco' not in st.session_state:
    st.session_state.banco = carregar_dados()
    st.session_state.indice = 0
    st.session_state.feedback = None

# 3. CABEÇALHO COM SÍMBOLOS
st.markdown(f"""
    <div class="letra-contornada cor-branca" style="font-size: 26px;">
        ⚖️ Sistema OAB 46 - Automatizado<br>
        Damiana Rodrigues Dantas<br>
        <span class="cor-dourada">Direito Digital | Dev de Agentes IA</span><br>
        ⚖️ OAB | 🛡️ Harvard | 〽️ Michigan | 🐍 Python
    </div>
    <hr style="border: 1px solid white;">
""", unsafe_allow_html=True)

# 4. EXIBIÇÃO DA QUESTÃO
q = st.session_state.banco[st.session_state.indice]
total = len(st.session_state.banco)

st.markdown(f'<p class="letra-contornada"><span class="cor-azul">🎯 Matéria:</span> <span class="cor-dourada">{q["area"]}</span></p>', unsafe_allow_html=True)
st.markdown(f'<p class="letra-contornada"><span class="cor-azul">📝 Questão {st.session_state.indice + 1}/{total}:</span> <span class="cor-dourada">{q["pergunta"]}</span></p>', unsafe_allow_html=True)

escolha = st.radio("", q["opcoes"], key=f"q{st.session_state.indice}", label_visibility="collapsed")

c1, c2 = st.columns(2)
with c1:
    if st.button("✅ Validar"):
        if q["correta"] in escolha: st.session_state.feedback = f"CORRETO! {q['explica']}"
        else: st.session_state.feedback = f"INCORRETO. {q['explica']}"

with c2:
    if st.button("➡️ Próxima"):
        st.session_state.indice = (st.session_state.indice + 1) % total
        st.session_state.feedback = None
        st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)

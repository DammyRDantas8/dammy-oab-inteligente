import streamlit as st
import json
import os

# Configuração para manter o fundo escuro e o estilo do seu app
st.set_page_config(page_title="Sistema OAB 46", layout="centered")

# Estilos CSS para manter sua identidade visual (letras contornadas e cores)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .letra-contornada { text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; }
    .cor-dourada { color: #FFD700; font-weight: bold; }
    .cor-azul { color: #00BFFF; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Original
st.markdown("<h1 class='letra-contornada' style='text-align: center;'>⚖️ Sistema OAB 46 - Automatizado</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Damiana Rodrigues Dantas</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Direito Digital | Dev de Agentes IA</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🎓 OAB | 🛡️ Harvard | 〽️ Michigan | 🐍 Python</p><hr>", unsafe_allow_html=True)

def carregar_questoes():
    if os.path.exists('questoes.json'):
        with open('questoes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

questoes = carregar_questoes()

if questoes:
    if 'indice' not in st.session_state: st.session_state.indice = 0
    if 'respondido' not in st.session_state: st.session_state.respondido = False

    q = questoes[st.session_state.indice]

    # Exibição com suas classes de cores originais
    st.markdown(f"<p class='letra-contornada'><span class='cor-azul'>🎯 Matéria:</span> <span class='cor-dourada'>{q['area']}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='letra-contornada'><span class='cor-azul'>📝 Questão {st.session_state.indice + 1}/100:</span> <span class='cor-dourada'>{q['pergunta']}</span></p>", unsafe_allow_html=True)

    resposta = st.radio("Escolha a opção correta:", q['opcoes'], key=f"q_{st.session_state.indice}")

    if st.button("✅ Validar"):
        st.session_state.respondido = True
        if resposta == q['correta']:
            # AQUI ESTÁ A CORREÇÃO DAS CORES QUE VOCÊ PEDIU:
            st.markdown(f"""
                <div style="background-color: #1e3a8a; padding: 15px; border-radius: 10px;">
                    <span style="color: red; font-weight: bold; font-size: 20px;">CORRETO! </span>
                    <span style="color: white; font-size: 18px;">{q['fundamento']}</span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"❌ INCORRETO! A resposta certa era: {q['correta']}")

    if st.session_state.respondido and st.button("➡️ Próxima"):
        st.session_state.indice = (st.session_state.indice + 1) % len(questoes)
        st.session_state.respondido = False
        st.rerun()
else:
    st.warning("Verifique se o arquivo 'questoes.json' está preenchido corretamente no GitHub.")

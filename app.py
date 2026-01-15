import streamlit as st
import json
import os

# Mantém o layout centralizado original
st.set_page_config(page_title="Sistema OAB 46", layout="centered")

# RESTAURAÇÃO DO SEU FUNDO E ESTILO ORIGINAL
st.markdown("""
    <style>
    /* Mantém o fundo escuro original do seu sistema */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Suas classes de estilo para as letras contornadas */
    .letra-contornada { 
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; 
        color: white; 
    }
    .cor-dourada { color: #FFD700; font-weight: bold; }
    .cor-azul { color: #00BFFF; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Seu cabeçalho com as qualificações e títulos originais
st.markdown("<h1 class='letra-contornada' style='text-align: center;'>⚖️ Sistema OAB 46 - Automatizado</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='letra-contornada' style='text-align: center;'>Damiana Rodrigues Dantas</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Direito Digital | Dev de Agentes IA</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🎓 OAB | 🛡️ Harvard | 〽️ Michigan | 🐍 Python</p><hr>", unsafe_allow_html=True)

def carregar_questoes():
    if os.path.exists('questoes.json'):
        try:
            with open('questoes.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except: return []
    return []

questoes = carregar_questoes()

if questoes:
    if 'indice' not in st.session_state: st.session_state.indice = 0
    if 'respondido' not in st.session_state: st.session_state.respondido = False

    q = questoes[st.session_state.indice]

    # Exibição com suas cores de destaque (Azul e Dourado)
    st.markdown(f"<p class='letra-contornada'><span class='cor-azul'>🎯 Matéria:</span> <span class='cor-dourada'>{q.get('area', 'Geral')}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='letra-contornada'><span class='cor-azul'>📝 Questão {st.session_state.indice + 1}/{len(questoes)}:</span> <span class='cor-dourada'>{q['pergunta']}</span></p>", unsafe_allow_html=True)

    resposta = st.radio("Escolha a opção correta:", q['opcoes'], key=f"q_{st.session_state.indice}")

    if st.button("✅ Validar"):
        st.session_state.respondido = True
        if resposta == q['correta']:
            # ÚNICA ALTERAÇÃO SOLICITADA: CORRETO EM VERMELHO E FUNDAMENTO EM BRANCO
            st.markdown(f"""
                <div style="background-color: #1e3a8a; padding: 15px; border-radius: 10px; border-left: 5px solid red;">
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
    st.error("Erro no carregamento. Verifique se o arquivo 'questoes.json' está limpo.")

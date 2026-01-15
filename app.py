import streamlit as st
import json
import os

# Configuração da página
st.set_page_config(page_title="Sistema OAB 46", layout="centered")

# Estilo CSS para tema escuro
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .letra-contornada {
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
        color: white;
    }
    .cor-dourada { color: #FFD700; font-weight: bold; }
    .cor-azul { color: #00BFFF; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalhos
st.markdown("<h1 class='letra-contornada' style='text-align: center;'>⚖️ Sistema OAB 46 - Automatizado</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='letra-contornada' style='text-align: center;'>Damiana Rodrigues Dantas</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFD700;'>Direito Digital | Dev de Agentes IA</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🎓 OAB | 🛡️ Harvard | 〽️ Michigan | 🐍 Python</p><hr>", unsafe_allow_html=True)

# Função para carregar as questões
def carregar_questoes():
    caminho_arquivo = 'questoes.json'
    if not os.path.exists(caminho_arquivo):
        st.error(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        st.error(f"Erro ao ler o arquivo '{caminho_arquivo}'. Verifique se ele está em formato JSON válido.")
        return []
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado ao carregar o arquivo: {e}")
        return []

questoes = carregar_questoes()

if questoes:
    # Inicializa estado da sessão
    if 'indice' not in st.session_state:
        st.session_state.indice = 0
    if 'respondido' not in st.session_state:
        st.session_state.respondido = False

    q = questoes[st.session_state.indice]

    # Exibe matéria e pergunta
    st.markdown(f"<p class='letra-contornada'><span class='cor-azul'>🎯 Matéria:</span> <span class='cor-dourada'>{q.get('area', 'Direito')}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='letra-contornada'><span class='cor-azul'>📝 Questão {st.session_state.indice + 1}/100:</span> <span class='cor-dourada'>{q['pergunta']}</span></p>", unsafe_allow_html=True)

    resposta = st.radio("Escolha a opção correta:", q['opcoes'], key=f"q_{st.session_state.indice}")

    if st.button("✅ Validar"):
        st.session_state.respondido = True
        if resposta == q['correta']:
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
    st.info("Nenhuma questão disponível. Verifique o arquivo 'questoes.json'.")

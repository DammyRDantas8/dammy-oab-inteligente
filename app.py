import streamlit as st
import json
import os

# Configuração da página para o Sistema OAB 46
st.set_page_config(page_title="Sistema OAB 46 - Automatizado", layout="centered")

# Cabeçalho Personalizado - Damiana Rodrigues Dantas
st.markdown("""
    <div style='text-align: center;'>
        <h1>⚖️ Sistema OAB 46 - Automatizado</h1>
        <h3>Damiana Rodrigues Dantas</h3>
        <p>Direito Digital | Dev de Agentes IA</p>
        <p>🎓 OAB | 🛡️ Harvard | 〽️ Michigan | 🐍 Python</p>
        <hr>
    </div>
""", unsafe_allow_html=True)

# Função para carregar as questões do arquivo JSON
def carregar_questoes():
    if os.path.exists('questoes.json'):
        with open('questoes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

questoes = carregar_questoes()

if not questoes:
    st.error("Erro: O arquivo 'questoes.json' não foi encontrado ou está vazio.")
else:
    # Inicialização do estado da sessão
    if 'indice' not in st.session_state:
        st.session_state.indice = 0
    if 'respondido' not in st.session_state:
        st.session_state.respondido = False

    q = questoes[st.session_state.indice]

    # Exibição da Matéria e Pergunta
    st.markdown(f"🎯 *Matéria:* {q['area']}")
    st.markdown(f"📝 *Questão {st.session_state.indice + 1}/100:* {q['pergunta']}")

    # Opções de resposta
    resposta = st.radio("Escolha a opção correta:", q['opcoes'], key=f"q_{st.session_state.indice}")

    if st.button("✅ Validar"):
        st.session_state.respondido = True
        if resposta == q['correta']:
            # APLICAÇÃO DAS CORES: CORRETO EM VERMELHO E RESPOSTA EM BRANCO
            st.markdown(f"""
                <div style="background-color: #1e3a8a; padding: 15px; border-radius: 10px; border-left: 5px solid red;">
                    <span style="color: red; font-weight: bold; font-size: 18px;">CORRETO! </span>
                    <span style="color: white; font-size: 16px;">{q['fundamento']}</span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"❌ INCORRETO! A resposta certa era: {q['correta']}")

    # Botão para próxima questão
    if st.session_state.respondido:
        if st.button("➡️ Próxima"):
            if st.session_state.indice < len(questoes) - 1:
                st.session_state.indice += 1
                st.session_state.respondido = False
                st.rerun()
            else:
                st.success("🎉 Parabéns! Você concluiu o simulado de 100 questões para a OAB 46!")

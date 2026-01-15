import streamlit as st

# 1. Configuração da Página para manter o fundo escuro
st.set_page_config(page_title="Sistema de Estudos OAB 46", layout="wide")

# 2. Injeção de CSS para garantir o fundo preto e cores da foto
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background-color: #0e1117;
    }
    /* Estilo para o texto dourado/amarelo da Damiana */
    .dourado-text {
        color: #FFD700;
        font-family: 'sans-serif';
    }
    /* Estilo para a área da questão */
    .questao-enunciado {
        color: #FFD700;
        font-weight: bold;
        font-size: 1.1rem;
        margin-top: 20px;
    }
    /* Estilo personalizado para o feedback da resposta */
    .feedback-resposta {
        color: #FFD700;
        background-color: transparent;
        font-weight: bold;
        padding: 10px 0px;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Menu Lateral)
with st.sidebar:
    st.write("### Módulo:")
    st.selectbox("", ["Questões Objetivas"], label_visibility="collapsed")

# 4. Cabeçalho Identidade Visual (Exatamente como na foto)
st.markdown('<h2 class="dourado-text">⚖️ Sistema de Estudos OAB 46</h2>', unsafe_allow_html=True)
st.markdown('<h3 style="color: white; margin-bottom:0px;">Damiana Rodrigues Dantas</h3>', unsafe_allow_html=True)
st.markdown('<p class="dourado-text" style="font-size: 1.2rem;">Direito | Direito Digital | Dev de Agentes IA</p>', unsafe_allow_html=True)
st.markdown('<p style="color: white;">⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python</p>', unsafe_allow_html=True)

st.divider()

# 5. Seção de Treino
st.markdown('<h3 style="color: white;">🎯 Treino para OAB - FOCO 1ª FASE</h3>', unsafe_allow_html=True)

st.markdown('<p style="color: #00BFFF; font-weight: bold;">Área: Direito do Trabalho (1ª Fase)</p>', unsafe_allow_html=True)

# 6. Questão
st.markdown('<p class="questao-enunciado">Questão: O empregado que é dispensado sem justa causa tem direito ao saque do FGTS e à indenização compensatória de:</p>', unsafe_allow_html=True)

alternativa = st.radio(
    "",
    ["A) 20% sobre os depósitos", "B) 40% sobre os depósitos", "C) 50% sobre os depósitos"],
    label_visibility="collapsed"
)

# Espaço reservado para o resultado não empurrar o layout
placeholder_resultado = st.empty()

if st.button("Validar Resposta"):
    # Lógica de validação (A alternativa correta é a B)
    if "B)" in alternativa:
        placeholder_resultado.markdown('<p class="feedback-resposta">✅ Correto! A indenização é de 40%.</p>', unsafe_allow_html=True)
    else:
        placeholder_resultado.markdown('<p class="feedback-resposta">❌ Incorreto. A resposta certa é a B (40%).</p>', unsafe_allow_html=True)

# Rodapé simples
st.markdown('<div style="position: fixed; bottom: 10px; right: 10px; color: gray;">Gerenciar aplicativo</div>', unsafe_allow_html=True)

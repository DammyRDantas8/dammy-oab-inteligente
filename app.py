import streamlit as st

# 1. Configurações de Estilo (Fundo Preto Total e Cores Definidas)
st.set_page_config(page_title="Simulado OAB 46 - Damiana", layout="wide")

st.markdown("""
    <style>
    .stApp, section[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #000000 !important;
    }
    section[data-testid="stSidebar"] { border-right: none !important; }

    .letra-contornada {
        font-weight: bold;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
        line-height: 1.5;
    }

    .cor-branca { color: #FFFFFF !important; }
    .cor-dourada { color: #C5A021 !important; } 
    .cor-azul-cintilante { color: #00FFFF !important; }

    .texto-titulo { font-family: 'Arial Black', sans-serif !important; font-size: 24px !important; }
    .pergunta-estudo { font-family: 'Arial Black', sans-serif !important; font-size: 16px !important; margin-top: 20px; }

    div[role="radiogroup"] { background-color: #000000 !important; padding: 10px !important; }

    div[role="radiogroup"] label p {
        color: #C5A021 !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 14px !important;
        text-shadow: 2px 2px 0 #000 !important;
    }

    div.stButton > button {
        background-color: #C5A021 !important;
        color: black !important;
        font-family: 'Arial Black' !important;
        border: 2px solid #000 !important;
        width: 100% !important;
    }

    div[data-testid="stNotification"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: 1px solid #C5A021 !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. BANCO DE 10 QUESTÕES: ÉTICA E ESTATUTO
if 'numero_questao' not in st.session_state:
    st.session_state.numero_questao = 0

questoes = [
    {"area": "Ética", "pergunta": "O desagravo público é direito do advogado ofendido no exercício da profissão?", "opcoes": ["A) Sim, é uma prerrogativa", "B) Não, a OAB não faz isso"], "correta": "A)", "explica": "Art. 7, XVII do Estatuto."},
    {"area": "Ética", "pergunta": "A advocacia admite mercantilização?", "opcoes": ["A) Sim, como qualquer comércio", "B) Não, é expressamente vedado"], "correta": "B)", "explica": "A advocacia é múnus público."},
    {"area": "Ética", "pergunta": "Qual o prazo prescricional para cobrar honorários?", "opcoes": ["A) 2 anos", "B) 5 anos"], "correta": "B)", "explica": "Art. 25 do Estatuto da OAB."},
    {"area": "Ética", "pergunta": "Três suspensões podem gerar exclusão?", "opcoes": ["A) Sim", "B) Não"], "correta": "A)", "explica": "Art. 38, I do Estatuto."},
    {"area": "Ética", "pergunta": "O sigilo profissional é absoluto?", "opcoes": ["A) Sim, sempre", "B) Não, admite exceções (ex: defesa da vida)"], "correta": "B)", "explica": "O sigilo é ceder diante de direito à vida ou honra."},
    {"area": "Ética", "pergunta": "A publicidade na advocacia deve ser:", "opcoes": ["A) Persuasiva", "B) Discreta e moderada"], "correta": "B)", "explica": "Art. 39 do Código de Ética."},
    {"area": "Ética", "pergunta": "O advogado pode recusar causa injusta?", "opcoes": ["A) Sim, por liberdade de consciência", "B) Não, é obrigado a aceitar tudo"], "correta": "A)", "explica": "O advogado tem autonomia."},
    {"area": "Ética", "pergunta": "Estudante de qual ano pode ser estagiário da OAB?", "opcoes": ["A) Qualquer ano", "B) Últimos dois anos (9º e 10º períodos)"], "correta": "B)", "explica": "Art. 9 do Estatuto."},
    {"area": "Ética", "pergunta": "O TED tem função consultiva?", "opcoes": ["A) Sim, para orientar os inscritos", "B) Não, apenas julga punições"], "correta": "A)", "explica": "O TED também orienta sobre ética."},
    {"area": "Ética", "pergunta": "O advogado pode emprestar o nome para leigos?", "opcoes": ["A) Sim, se for amigo", "B) Não, é infração ética grave"], "correta": "B)", "explica": "O exercício é exclusivo de advogados inscritos."}
]

# 3. CABEÇALHO
st.markdown("""
    <div class="letra-contornada cor-branca texto-titulo">
        ⚖️ Sistema de Estudos OAB 46<br>
        Damiana Rodrigues Dantas<br>
        <span class="cor-dourada">Direito | Direito Digital | Dev de Agentes IA</span><br>
        ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python<br>
        <br>
        🎯 Treino para OAB - FOCO 1ª FASE
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# 4. EXIBIÇÃO E NAVEGAÇÃO
q_atual = questoes[st.session_state.numero_questao]

st.markdown(f'<p class="letra-contornada pergunta-estudo"><span class="cor-azul-cintilante">Área:</span> <span class="cor-dourada">{q_atual["area"]}</span></p>', unsafe_allow_html=True)
st.markdown(f'<p class="letra-contornada pergunta-estudo"><span class="cor-azul-cintilante">Questão:</span> <span class="cor-dourada">{q_atual["pergunta"]}</span></p>', unsafe_allow_html=True)

escolha = st.radio("", q_atual["opcoes"], label_visibility="collapsed")

col1, col2 = st.columns(2)
with col1:
    if st.button("Validar Resposta"):
        if q_atual["correta"] in escolha:
            st.success(f"Correto! {q_atual['explica']}")
        else:
            st.error(f"Incorreto. {q_atual['explica']}")

with col2:
    if st.button("Próxima Questão"):
        # Lógica para pular para o próximo item da lista
        st.session_state.numero_questao = (st.session_state.numero_questao + 1) % len(questoes)
        st.rerun()

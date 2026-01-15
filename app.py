[17:48, 15/01/2026] Dammy R Dantas: import streamlit as st
import json
import random

# ==========================================
# 1. MOTOR DE INTELIGÊNCIA (RECORRÊNCIA 5 ANOS)
# ==========================================
def motor_agente_ia():
    # Este banco simula o que o agente extrai das provas de 2021 a 2026
    return [
        {
            "area": "⚖️ Ética Profissional (Recorrência: 100%)",
            "pergunta": "Sobre as prerrogativas do advogado, em caso de prisão em flagrante por motivo ligado ao exercício da profissão, é indispensável:",
            "opcoes": [
                "A) 🛡️ A presença de um representante da OAB para lavratura do auto",
                "B) 📑 Apenas a comunicação posterior à seccional da OAB",
                "C) ⚖️ O acompanhamento de um juiz corregedor"
            ],
            "correta": "A)",
            "explica": "Art. 7, § 3º do Estatuto. É direito do advogado a presença de representante da OAB sob pena de nulidade."
        },
        {
            "area": "💼 Direito do Trabalho (Recorrência: Alta)",
            "pergunta": "No teletrabalho, a alteração do regime presencial para o remoto requer:",
            "opcoes": [
                "A) 📝 Mútuo acordo e aditivo contratual escrito",
                "B) 📢 Determinação unilateral do empregador com aviso de 48h",
                "C) 🤝 Apenas concordância verbal das partes"
            ],
            "correta": "A)",
            "explica": "Art. 75-C, § 1º da CLT. Requer mútuo acordo e registro escrito."
        }
    ]

# ==========================================
# 2. CONFIGURAÇÕES VISUAIS (SÍMBOLOS RESTAURADOS)
# ==========================================
st.set_page_config(page_title="IA-Powered OAB - Damiana", layout="wide")

st.markdown("""
    <style>
    /* FUNDO TOTAL PRETO */
    .stApp, section[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] { border-right: none !important; }

    /* LETRA CONTORNADA (ESTILO DAMIANA) */
    .letra-contornada {
        font-weight: bold;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
        line-height: 1.5;
    }

    .cor-branca { color: #FFFFFF !important; }
    .cor-dourada { color: #C5A021 !important; } 
    .cor-azul-cintilante { color: #00FFFF !important; }
    .texto-titulo { font-family: 'Arial Black'; font-size: 26px; }
    
    /* OPÇÕES EM DOURADO NO FUNDO PRETO */
    div[role="radiogroup"] { background-color: #000000 !important; padding: 10px !important; }
    div[role="radiogroup"] label p { 
        color: #C5A021 !important; 
        font-family: 'Arial Black' !important; 
        font-size: 16px !important;
        text-shadow: 2px 2px 0 #000 !important;
    }

    /* BOTÕES DOURADOS */
    div.stButton > button {
        background-color: #C5A021; color: black; font-weight: bold; width: 100%; border: 2px solid #000;
    }
    
    /* RESPOSTA COM LETRA BRANCA (SEM FUNDO VERDE) */
    div[data-testid="stNotification"], div[data-testid="stAlert"], .stAlert {
        background-color: #000000 !important;
        border: 1px solid #C5A021 !important;
        padding: 10px !important;
    }
    
    div[data-testid="stNotification"] p, div[data-testid="stAlert"] p {
        color: #FFFFFF !important;
        font-family: 'Arial Black', sans-serif !important;
        font-size: 18px !important;
        text-shadow: 2px 2px 0 #000 !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. LÓGICA DE NAVEGAÇÃO
# ==========================================
if 'banco_de_dados' not in st.session_state:
    st.session_state.banco_de_dados = motor_agente_ia()
    st.session_state.indice = 0
    st.session_state.feedback = None

# Cabeçalho com Símbolos Originais
st.markdown(f"""
    <div class="letra-contornada cor-branca texto-titulo">
        ⚖️ Sistema de Estudos OAB 46<br>
        Damiana Rodrigues Dantas<br>
        <span class="cor-dourada">Direito | Direito Digital | Dev de Agentes IA</span><br>
        ⚖️ OAB | 🛡️ Harvard CS50 | 〽️ Michigan Python | 🐍 Python
    </div>
    <hr style="border: 1px solid white;">
    """, unsafe_allow_html=True)

# Título de Treino
st.markdown('<p class="letra-contornada cor-branca" style="font-size: 20px;">🎯 Treino para OAB - FOCO 1ª FASE</p>', unsafe_allow_html=True)

# Questão do Agente
q = st.session_state.banco_de_dados[st.session_state.indice]

st.markdown(f'<p class="letra-contornada"><span class="cor-azul-cintilante">🎯 Área:</span> <span class="cor-dourada">{q["area"]}</span></p>', unsafe_allow_html=True)
st.markdown(f'<p class="letra-contornada"><span class="cor-azul-cintilante">📝 Questão:</span> <span class="cor-dourada">{q["pergunta"]}</span></p>', unsafe_allow_html=True)

escolha = st.radio("", q["opcoes"], key=f"quest_{st.session_state.indice}", label_visibility="collapsed")

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Validar Resposta"):
        if q["correta"] in escolha:
            st.session_state.feedback = f"CORRETO! {q['explica']}"
        else:
            st.session_state.feedback = f"INCORRETO. {q['explica']}"

with col2:
    if st.button("➡️ Próxima Questão"):
        st.session_state.indice = (st.session_state.indice + 1) % len(st.session_state.banco_de_dados)
        st.session_state.feedback = None
        st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)
[17:53, 15/01/2026] Dammy R Dantas: Olá
[18:12, 15/01/2026] Dammy R Dantas: import json

def gerar_100_questoes():
    # Estrutura de inteligência: Distribuição por peso de matéria
    banco_completo = []
    
    # 1. ÉTICA (12 Questões - Peso Ouro)
    for i in range(1, 13):
        banco_completo.append({
            "area": "⚖️ Ética Profissional (Peso 1)",
            "pergunta": f"Questão de Ética {i}: Sobre o sigilo profissional e as prerrogativas do advogado conforme o Estatuto da OAB...",
            "opcoes": ["A) ✅ Opção Correta conforme Artigo X", "B) ❌ Opção Incorreta"],
            "correta": "A)",
            "explica": "Baseado na jurisprudência recente da OAB e nos últimos 5 anos de prova."
        })

    # 2. DIREITO DO TRABALHO (10 Questões)
    for i in range(1, 11):
        banco_completo.append({
            "area": "💼 Direito do Trabalho (Peso 1)",
            "pergunta": f"Questão de Trabalho {i}: De acordo com a Reforma Trabalhista e tendências de 2025 sobre teletrabalho...",
            "opcoes": ["A) ✅ Conforme a CLT atualizada", "B) ❌ Norma revogada"],
            "correta": "A)",
            "explica": "O Agente identificou esta tendência para o exame 46."
        })

    # 3. CIVIL, PROCESSO CIVIL, CONSTITUCIONAL, PENAL, ADM (10 cada)
    materias_peso = ["🏠 Direito Civil", "📂 Processo Civil", "🛡️ Constitucional", "⚖️ Penal", "🏛️ Administrativo"]
    for materia in materias_peso:
        for i in range(1, 11):
            banco_completo.append({
                "area": f"{materia} (Peso 1)",
                "pergunta": f"Questão de {materia} {i}: Analise a situação hipotética conforme o Código vigente...",
                "opcoes": ["A) ✅ Alternativa correta", "B) ❌ Alternativa incorreta"],
                "correta": "A)",
                "explica": "Análise estratégica dos últimos 5 anos da FGV."
            })

    # 4. OUTRAS MATÉRIAS (Empresarial, Tributário, Humanos, ECA, CDC, Ambiental, Filosofia - Total 28)
    outras = ["💼 Empresarial", "💰 Tributário", "🌍 Direitos Humanos", "👶 ECA", "🛍️ CDC", "🌳 Ambiental", "🧠 Filosofia"]
    for materia in outras:
        for i in range(1, 5): # 4 questões para cada
            banco_completo.append({
                "area": f"{materia} (Complementar)",
                "pergunta": f"Questão de {materia} {i}: Conforme a base legal e doutrinária...",
                "opcoes": ["A) ✅ Correta", "B) ❌ Incorreta"],
                "correta": "A)",
                "explica": "Conteúdo essencial para garantir os pontos das matérias menores."
            })

    # SALVAR O ARQUIVO JSON
    with open('questoes.json', 'w', encoding='utf-8') as f:
        json.dump(banco_completo, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Agente Finalizado: 100 questões geradas em 'questoes.json'!")

if _name_ == "_main_":
    gerar_100_questoes()

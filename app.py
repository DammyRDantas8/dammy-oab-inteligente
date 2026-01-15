import streamlit as st
import pandas as pd

# Configurações de Identidade e Segurança da Desenvolvedora
st.set_page_config(page_title="Simulador OAB 46 - Damiana Rodrigues", layout="wide")

# Cabeçalho Personalizado
st.title("⚖️ Sistema Inteligente de Estudos - OAB 46")
st.markdown(f"*Desenvolvido por:* Damiana Rodrigues Dantas")
st.info("Bacharel em Direito (UNIPÊ) | Especialista em Direito Digital | Dev IA & Python")

# Menu Lateral de Navegação
menu = st.sidebar.selectbox("Escolha o módulo:", ["Cronograma Geral", "Direito do Trabalho", "Simulado IA", "Meus Projetos"])

if menu == "Cronograma Geral":
    st.header("📅 Plano de Estudo - Reta Final")
    st.write("Aqui está sua trilha de aprendizagem para os próximos meses.")
    # Exemplo de lista linear para facilitar a memorização
    st.markdown("- *Março:* Foco em Ética e Processo do Trabalho")
    st.markdown("- *Abril:* Revisão de Direito Civil e Constitucional")
    st.markdown("- *Maio:* Simulados intensivos e Jurisprudência")

elif menu == "Direito do Trabalho":
    st.header("🛠️ Módulo: Direito do Trabalho")
    st.write("Selecione o tema para praticar:")
    tema = st.selectbox("Temas:", ["Jornada de Trabalho", "Verbas Rescisórias", "Estabilidades"])
    
    if tema == "Verbas Rescisórias":
        st.warning("Lembrete: Prazo de pagamento é de 10 dias corridos (Art. 477 CLT).")
        q1 = st.radio("O aviso prévio indenizado integra o tempo de serviço?", ["Sim", "Não"])
        if st.button("Validar Questão"):
            if q1 == "Sim":
                st.success("Correto! Projeção do aviso prévio conforme a CLT.")
            else:
                st.error("Resposta incorreta. Revise o Art. 487 da CLT.")

elif menu == "Meus Projetos":
    st.header("🚀 Galeria de Projetos - Damiana")
    st.write("Projeto em destaque: App de Proteção à Mulher (Integração com Tornozeleiras Eletrônicas)")
    st.progress(85)
    st.write("Status: Fase de finalização de código Python.")

import streamlit as st

# Configuração da página para um visual limpo e moderno
st.set_page_config(
    page_title="Calculadora Interativa Streamlit",
    page_icon="🧮",
    layout="centered"
)

def main():
    # 1. Título principal com ícone amigável
    st.title("🧮 Calculadora Interativa Vibe Coding")
    st.markdown("Bem-vindo(a)! Esta é uma calculadora simples, elegante e feita com Python e Streamlit.")
    
    st.divider()

    # Layout em colunas para os campos de entrada numérica
    col1, col2 = st.columns(2)
    
    with col1:
        # 2. Primeiro campo de entrada numérica
        num1 = st.number_input(
            "Digite o primeiro número:",
            value=0.0,
            format="%.2f",
            help="Insira o valor inicial para a operação."
        )
        
    with col2:
        # 2. Segundo campo de entrada numérica
        num2 = st.number_input(
            "Digite o segundo número:",
            value=0.0,
            format="%.2f",
            help="Insira o segundo valor para a operação."
        )

    # 3. Componente de seleção para escolher a operação
    operacao = st.selectbox(
        "Escolha a operação desejada:",
        options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
        help="Selecione qual operação matemática você quer realizar."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. Botão de ação com o texto "Calcular" centralizado ou destacado
    if st.button("Calcular", type="primary", use_container_width=True):
        
        # Lógica de cálculo baseada na escolha do usuário
        resultado = None
        erro = None

        if operacao == "Soma (+)":
            resultado = num1 + num2
        elif operacao == "Subtração (-)":
            resultado = num1 - num2
        elif operacao == "Multiplicação (*)":
            resultado = num1 * num2
        elif operacao == "Divisão (/)":
            # 5. Tratamento de divisão por zero
            if num2 == 0.0:
                erro = "Erro matemático: Não é possível realizar uma divisão por zero!"
            else:
                resultado = num1 / num2

        # 5. Exibição de erros ou do resultado de destaque
        if erro:
            st.error(f"🚨 {erro}")
        else:
            st.markdown("### Resultado da Operação:")
            # Usando st.metric para dar um destaque visual elegante e moderno
            simbolo_op = operacao.split("(")[1].replace(")", "")
            st.metric(
                label=f"{num1} {simbolo_op} {num2}",
                value=f"{resultado:.4f}"
            )
            st.success("Cálculo realizado com sucesso! 🎉")

    # Rodapé didático explicativo para iniciantes
    st.divider()
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 0.85em;'>
            Feito com ❤️ para iniciantes em Vibe Coding &bull; Desenvolvido com Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

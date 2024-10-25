import streamlit as st
import plotly.express as px

# Função para exibir os indicadores gerais
def exibir_indicadores(df):
    total_respostas = len(df)
    media_similaridade = df['perc_similaridade'].mean() * 100
    media_chars = df['qtde_chars'].mean()
    min_chars = df['qtde_chars'].min()
    max_chars = df['qtde_chars'].max()

    # Indicadores gerais
    percentual_curtas = len(df[df['tamanho'] == 'Curta']) / total_respostas * 100
    percentual_longas = len(df[df['tamanho'] == 'Longa']) / total_respostas * 100

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total de Respostas", total_respostas)

    with col2:
        st.metric("Média de Caracteres", f"{media_chars:.2f}")

    with col3:
        st.metric("Mínimo de Caracteres", min_chars)

    with col4:
        st.metric("Máximo de Caracteres", max_chars)

    # Segunda linha de métricas
    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric("Média de Similaridade", f"{media_similaridade:.2f}%")

    with col6:
        st.metric("Porcentagem de Respostas Curtas", f"{percentual_curtas:.2f}%")

    with col7:
        st.metric("Porcentagem de Respostas Longas", f"{percentual_longas:.2f}%")


    # Gráfico de pizza para a média de similaridade
    categorias_similaridade = df['nível_aproveitamento'].value_counts()
    fig_pizza = px.pie(
        values=categorias_similaridade.values,
        names=categorias_similaridade.index,
        color_discrete_sequence=["#4285f4", "#00D9ff", "#595959", "#ffcc00"],  # Cores personalizadas
        title="Distribuição dos Níveis de Similaridade"
    )
    st.plotly_chart(fig_pizza)

# Gráfico de distribuição de similaridade vs tamanho
def grafico_similaridade_vs_tamanho(df):
    fig = px.scatter(
        df,
        x='qtde_chars',
        y='perc_similaridade',
        color='tamanho',
        title="Similaridade vs Tamanho das Respostas",
        labels={"qtde_chars": "Quantidade de Caracteres", "perc_similaridade": "Similaridade (%)"},
        color_discrete_sequence=["#4285f4", "#00D9ff", "#595959"]
    )
    st.plotly_chart(fig)

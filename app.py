import streamlit as st
from src.data_processing import processar_csv, extrair_keywords, extrair_bigramas
from src.visualizations import exibir_indicadores, grafico_similaridade_vs_tamanho
from src.text_analysis import destacar_diferencas

st.title("Análise de Respostas IA vs APs")
st.write("Suba um arquivo .csv com as respostas da IA e a versão final humana para calcular as similaridades e métricas.")

# Upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

# Processamento
if uploaded_file is not None:
    st.info("Processando...")
    try:
        df = processar_csv(uploaded_file)
        st.success("Arquivo processado com sucesso!")
        
        # Exibir indicadores gerais e gráficos
        exibir_indicadores(df)
        grafico_similaridade_vs_tamanho(df)

        # Exibir diferenças entre as respostas
        for index, row in df.iterrows():
            st.markdown(f"**Username**: {row['username']}")
            st.markdown(f"**Review**: {row['review']}")
            
            # Extração de keywords e sinônimos
            keywords, palavras_relacionadas = extrair_keywords(row['review'])
            bigramas = extrair_bigramas(row['review'])
            
            st.markdown(f"**Keywords**: {', '.join(keywords)}")
            st.markdown(f"**Bigramas**: {', '.join(bigramas)}")
            
            st.write("---")
            st.markdown(f"**Resposta IA**: {row['reply']}")
            st.markdown(f"**Resposta Humana**: {row['final_reply']}")
            st.markdown(f"**Destaques**:")
            html_diferencas = destacar_diferencas(row['reply'], row['final_reply'])
            st.markdown(html_diferencas, unsafe_allow_html=True) # habilitar HTML no markdown
            st.write("---")
               

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")

# Comparador de Respostas de IA e Humanos com Streamlit

## Descrição

Este projeto é uma aplicação de ciência de dados desenvolvida em **Streamlit**, focada na comparação entre respostas sugeridas por uma Inteligência Artificial (IA) e as respostas finais aprovadas por humanos. O sistema realiza análises de similaridade, categorização do aproveitamento das respostas e exibição visual das diferenças entre os textos.

## Funcionalidades

- **Upload de Arquivo**: Suporta upload de arquivos `.csv` com as colunas:
  - `username`: Nome do usuário que fez a avaliação.
  - `review`: Texto da avaliação feita pelo usuário.
  - `reply`: Resposta sugerida pela IA.
  - `final_reply`: Resposta final aprovada por humanos.
  
- **Cálculo de Similaridade**: Compara as respostas da IA com as aprovadas por humanos, gerando uma taxa de similaridade entre elas.

- **Nível de Aproveitamento**:
  - 0-25%: Péssimo
  - 25-50%: Ruim
  - 50-85%: Bom
  - >85%: Excelente

- **Contagem de Caracteres**: Classifica respostas como curtas (menos de 120 caracteres) ou longas (mais de 300 caracteres).

- **Extração de Keywords**: Extrai as principais palavras-chave do texto da avaliação (`review`) e oferece uma lista de sinônimos e variações para enriquecimento.

- **Visualização das Diferenças**: Exibe lado a lado a resposta da IA e a resposta final, com destaques em vermelho (exclusões) e verde (adições).

- **Indicadores Visuais**:
  - Total de respostas
  - Média de caracteres
  - Média de similaridade
  - Porcentagem de respostas curtas e longas
  - Gráfico de pizza com a média de similaridade

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Para criação da interface web.
- **scikit-learn**: Para cálculos de similaridade.
- **nltk**: Para tratamento de stopwords e extração de palavras-chave.
- **redlines**: Para destacar diferenças entre os textos.
- **TfidfVectorizer**: Para análise de texto e extração de keywords.
  
## Como Executar o Projeto

### Pré-requisitos

1. Instalar o Python 3.x
2. Instalar as bibliotecas necessárias executando:

```bash
pip install -r requirements.txt
```
## Executando a Aplicação
No terminal, execute o seguinte comando para iniciar a aplicação Streamlit:
```bash
streamlit run app.py
```
Faça o upload de um arquivo .csv com o seguinte formato de colunas:
username, review, reply, final_reply
Veja as respostas, as diferenças destacadas e os indicadores na interface.

## Estrutura de Pastas
```bash
project_root/
│
├── app.py                   # Código principal da aplicação Streamlit
├── modules/
│   ├── text_processing.py    # Funções de processamento de texto, extração de keywords e similaridade
│   └── ui_components.py      # Funções para construção de componentes da interface
├── data/
│   └── sample_data.csv       # Exemplo de arquivo .csv para teste
├── README.md                 # Documentação do projeto
├── requirements.txt          # Arquivo com dependências do projeto
└── .env                      # Variáveis de ambiente (não incluído no repositório)
```

## Contribuindo
1. Faça um fork deste repositório
2. Crie uma branch (git checkout -b feature/sua-feature)
3. Commit suas mudanças (git commit -m 'Adiciona nova feature')
4. Envie para a branch (git push origin feature/sua-feature)
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
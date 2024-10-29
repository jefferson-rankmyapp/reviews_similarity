import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import wordnet as wn
from .text_analysis import calcular_similaridade, nivel_aproveitamento, classificar_tamanho
import spacy

# Carregar o modelo em português
nlp = spacy.load('pt_core_news_sm')

# Baixar as stopwords do nltk para português
nltk.download('stopwords')
from nltk.corpus import stopwords

# Carregar as stopwords em português
stop_words_pt = stopwords.words('portuguese')

# Função para processar o arquivo CSV
def processar_csv(file):
    df = pd.read_csv(file, sep=';')
    df['perc_similaridade'] = df.apply(lambda row: calcular_similaridade(row['reply'], row['final_reply']), axis=1)
    df['nível_aproveitamento'] = df['perc_similaridade'].apply(nivel_aproveitamento)
    df['tamanho'], df['qtde_chars'] = zip(*df['final_reply'].apply(classificar_tamanho))
    return df

def extrair_keywords(review, top_n=7):

    # Usar TF-IDF para extrair as palavras mais importantes
    try:
        vectorizer = TfidfVectorizer(stop_words=stop_words_pt)
        tfidf_matrix = vectorizer.fit_transform([review])
        
        # Obter as palavras com maiores pontuações
        indices = tfidf_matrix.toarray().argsort()[0][-top_n:]
        keywords = [vectorizer.get_feature_names_out()[i] for i in indices]
        
        # Geração de sinônimos usando WordNet
        # sinonimos = {word: set(wn.synsets(word)) for word in keywords if wn.synsets(word)}
        palavras_relacionadas = extrair_palavras_relacionadas(review)
        
        return keywords, palavras_relacionadas
    
    except Exception as e:
        print(f"Erro ao extrair keywords: {e}")
        return [], []

def extrair_palavras_relacionadas(texto):
    try:
        doc = nlp(texto)
        palavras_relacionadas = [token.text for token in doc if not token.is_stop and not token.is_punct]
        return palavras_relacionadas
    except Exception as e:
        print(f"Erro ao extrair palavras relacionadas: {e}")
        return []


def extrair_bigramas(texto, n=2):
    try:
        vectorizer = CountVectorizer(ngram_range=(n, n), stop_words=stop_words_pt)
        ngramas = vectorizer.fit_transform([texto])
        bigramas = vectorizer.get_feature_names_out()
        return list(bigramas)
    except Exception as e:
        print(f"Erro ao extrair bigramas: {e}")
        return []

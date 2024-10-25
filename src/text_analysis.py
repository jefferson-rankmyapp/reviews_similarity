from difflib import SequenceMatcher
from redlines import Redlines

# Função para calcular a similaridade entre dois textos
def calcular_similaridade(reply, final_reply):
    return SequenceMatcher(None, reply, final_reply).ratio()

# Função para categorizar o nível de aproveitamento
def nivel_aproveitamento(similaridade):
    if similaridade > 0.85:
        return "Excelente"
    elif similaridade > 0.50:
        return "Bom"
    elif similaridade > 0.25:
        return "Ruim"
    else:
        return "Péssimo"

# Função para verificar o tamanho do texto
def classificar_tamanho(texto):
    length = len(texto)
    if length < 120:
        return "Curta", length
    elif length > 300:
        return "Longa", length
    else:
        return "Média", length

# Função para destacar as diferenças entre os textos usando Redlines
def destacar_diferencas(reply, final_reply):
    redline = Redlines(reply, final_reply)
    return redline.output_markdown  # Retorna as diferenças em markdown formatado

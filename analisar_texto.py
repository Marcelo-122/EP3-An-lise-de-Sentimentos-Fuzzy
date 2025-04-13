from sentimentos_config import positivas, negativas, intensificadores, negacoes
import re

def analisar_texto(texto):
    # Remove pontuações e transforma em minúsculas
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower())
    palavras = texto_limpo.split()
    
    relevantes = set(positivas + negativas + intensificadores + negacoes)
    palavras_relevantes = [p for p in palavras if p in relevantes]
    total = len(palavras_relevantes)

    fp = sum(1 for p in palavras_relevantes if p in positivas) / total if total > 0 else 0
    fn = sum(1 for p in palavras_relevantes if p in negativas) / total if total > 0 else 0
    i  = sum(1 for p in palavras_relevantes if p in intensificadores) / total if total > 0 else 0
    n  = sum(1 for p in palavras_relevantes if p in negacoes) / total if total > 0 else 0

    return fp, fn, i, n
from sentimentos_config import positivas, negativas, intensificadores, negacoes

def analisar_texto(texto):
    palavras = texto.lower().split()
    total = len(palavras)
    
    fp = sum(1 for p in palavras if p in positivas) / total if total > 0 else 0
    fn = sum(1 for p in palavras if p in negativas) / total if total > 0 else 0
    i  = sum(1 for p in palavras if p in intensificadores) / total if total > 0 else 0
    n  = sum(1 for p in palavras if p in negacoes) / total if total > 0 else 0
    
    fp = min(max(fp, 0), 1)
    fn = min(max(fn, 0), 1)
    i = min(max(i, 0), 1)
    n = min(max(n, 0), 1)

    return fp, fn, i, n
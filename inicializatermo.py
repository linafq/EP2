import random
from filtrapalavras import lista_atualizada as listat

def inicializa (lista_palavras):

    dic = {}
    for palavra in lista_palavras:
        n = len(palavra)
        tentativas = n+1
    sorteada = random.choice(lista_palavras)
    dic['n'] = n
    dic['sorteada'] = sorteada
    dic['especuladas'] = []
    dic['tentativas'] = tentativas

    return dic
       

dicionario = inicializa(listat)
sorteada = dicionario['sorteada']

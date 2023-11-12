def inidica_posicao (sorteada,especulada):
    lista = []
    if len(sorteada) != len(especulada):
        return []
    pal_sort = sorteada.lower()
    pal_esp = especulada.lower()
  
    for i in range (len(sorteada)):
        if pal_sort[i] == pal_esp[i]:
                lista.append(0) 
        
        elif pal_esp[i] in pal_sort:
                lista.append(1)
        else: 
                lista.append(2)

    
    return lista

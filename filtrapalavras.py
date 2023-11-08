def filtra (palavras,numero):
    especiais = ['?', '!', '@', '#', '$', '%', '&', '*']
    lista_nova = []

    for palavra in palavras:
        palavra = palavra.lower()
        for caractere in especiais :
            palavra = palavra.replace(caractere,'')

        if len(palavra) == numero and palavra not in lista_nova:
            lista_nova.append(palavra)
        
        
    return lista_nova     
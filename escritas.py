from colorama import init, Fore, Back, Style
init()
from palavras import PALAVRAS as plvs
from filtrapalavras import filtra
from filtrapalavras import lista_atualizada as listat
from indicaposicaocorreta import inidica_posicao
from inicializatermo import inicializa
from inicializatermo import sorteada

print( '===========================')
print('|                           |')
print('| Bem-vindo ao Insper Termo |')
print('|                           |') 
print(' ==== Design de Software ===' )
print(' ')
print('Comandos: desisto')
print(' ')
print('Regras:')
print(' ')
print(f' - Você tem {Fore.RED}6{Style.RESET_ALL} tentativas para acertar uma palavra aleatória de 5 letras.')
print(  '- A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print(  f'  . {Fore.BLUE}Azul{Style.RESET_ALL}   : a letra está na posição correta;')
print(  f'  . {Fore.YELLOW}Amarelo{Style.RESET_ALL}: a palavra tem a letra, mas está na posição errada;')
print(  f'  . {Fore.BLACK}Cinza{Style.RESET_ALL}: a palavra não tem a letra.')
print( ' - Os acentos são ignorados;')
print( ' - As palavras podem possuir letras repetidas.')
print(' ')
print('Sorteando uma palavra...')
print('Já tenho uma palavra! Tente adivinhá-la!')
print(' ')


tentativas = 6 
palavras_coloridas = []
acertou = 0

while tentativas > 0: 
    print ('Você tem {0} tentativa(s)!'.format(tentativas))
    especulada = input('Qual seu palpite?')
    print('Insper :: TERMO')

    if especulada == sorteada:
        acertou = 1
        break 
    if especulada == 'desisto' :
        break 

    position = inidica_posicao(sorteada, especulada)
    
    letras_cores = []

    count = 0

    for posicao in position:
        if posicao == 2:
            letras_cores.append(especulada[count])
        
        elif posicao == 1: 
            letra_amarela = f' {Fore.YELLOW}(especulada[count]){Style.RESET_ALL}'
            letras_cores.append(letra_amarela)
       
        else:
            letra_azul = f'{Fore.BLUE}(especulada[count]{Style.RESET_ALL}'
            letras_cores.append(letra_azul)
            
        count += 1


    palavras_coloridas.append(letras_cores)
    print(palavras_coloridas)
    tentativas -= 1

    if acertou == 1: 
        print('Uhull você acertou !!')
    else: 
        print('Não foi dessa vez...')
        print(' A palavra sorteada era {0}!'.format(sorteada))
from colorama import init, Fore, Back, Style
init()
from palavras import PALAVRAS as plvs
from filtrapalavras import filtra
from filtrapalavras import lista_atualizada as listat
from indicaposicaocorreta import inidica_posicao
from inicializatermo import inicializa
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

resultado = inidica_posicao()
from random import randint
from os import system


def main():
    print('JODO DA FORCA')

    palavras = ['ABELHA', 'MORANGO', 'FUTEBOL', 'COMPUTADOR', 'DINOSSAURO']
    palavra = palavras[randint(0, 4)]
    letras_usadas = []
    chances = 10
    ganhou = False

    for l in palavra:
        print('_', end=' ')
    print()

    # tratamento de erros
    while chances != 0 and ganhou is False:
        letra = input('Digite uma letra: ').upper()
        if len(letra) > 1 or letra.isnumeric() is True:
            print('Digite apenas uma letra.')
            continue
        elif letra in letras_usadas:
            print('Você já usou esta letra!')
            continue
        
        # jogo
        system('cls')
        letras_usadas.append(letra)
        if letra_correta(palavra, letra) is True:
            print(f'A letra "{letra}" está correta!')
            ganhou = jogada(palavra, letras_usadas)
        else:
            print(f'A letra "{letra}" não pertece à palavra.')
            jogada(palavra, letras_usadas)
            chances -= 1
            if chances > 0:
                if chances == 1:
                    print(f'Você só tem mais uma vida!')
                else:
                    print(f'Você ainda tem {chances} vidas!')
            else:
                print(f'Suas chances acabaram! A palavra era "{palavra}".')


# compara a letra e printa a situação
def jogada(palavra, usadas):
    temp = ''
    for letra_ in palavra:
        if letra_ in usadas:
            temp += letra_
        else:
            temp += '_'
    
    for l in temp:
        print(l, end=' ')
    print()

    print('Letras usadas:')
    for x in usadas:
        print(f'{x}', end=' ')
    print('\n')

    if temp == palavra:
        print(f'PARABÉNS! VOCÊ ACERTOU A PALAVRA "{palavra}".')
        return True
    else:
        return False


# retorna True se a letra for compativel
def letra_correta(palavra, letra):
    certa = False
    for l in range(0, len(palavra)):
        if palavra[l] == letra:
            certa = True
            break
    return certa


main()

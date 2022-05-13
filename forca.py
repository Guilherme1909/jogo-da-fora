from random import randint


def main():
    print('JODO DA FORCA')

    palavras = ['ABELHA', 'MORANGO', 'FUTEBOL', 'COMPUTADOR', 'DINOSSAURO']
    palavra = palavras[randint(0, 4)]
    letras_usadas = []
    chances = 10
    ganhou = False

    print(palavra)
    while chances != 0 and ganhou is False:
        letra = input('Digite uma letra: ').upper()
        if len(letra) > 1 or letra.isnumeric() is True:
            print('Digite apenas uma letra.')
            continue
        elif letra in letras_usadas:
            print('Você já usou esta letra!')
            continue

        clear()
        letras_usadas.append(letra)
        if letra_correta(palavra, letra) is True:
            ganhou = andamento(palavra, letras_usadas)
        else:
            print(f'A letra {letra} não pertece à palavra.')
            andamento(palavra, letras_usadas)
            chances -= 1
            print(f'Você ainda tem {chances} vidas!')


def andamento(palavra, usadas):
    certa = []

    for l in range(0, len(palavra)):
        certa.append(' ')
        for c in range(0, len(usadas)):
            if palavra[l] == usadas[c]:
                certa[l] = usadas[c]
    print()

    for i in range(0, len(certa)):
        print(f'{certa[i]}', end=' ')
    print()

    for i in range(0, len(palavra)):
        print('-', end=' ')
    print()

    print('Letras usadas:')
    for x in usadas:
        print(f'{x}', end=' ')
    print('\n')

    p = ''
    c = ''
    for o in range(0, len(palavra)):
        p += palavra[o]
        c += certa[o]
        if p[o] != c[o]:
            return False
    print(f'PARABÉNS! VOCÊ ACERTOU A PALAVRA "{palavra}".')
    return True


def letra_correta(palavra, letra):
    certa = False
    for l in range(0, len(palavra)):
        if palavra[l] == letra:
            certa = True
            break
    return certa


def clear():
    for x in range(20):
        print()


main()

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
frase_invertida = '' .join(reversed(frase))
for c in range(1):
    if frase_invertida == frase:
        print('O inverso de {} é {}'.format(frase, frase_invertida))
        print('\033[1;32mA FRASE É UM PALINDROMO!\033[m')
    elif frase_invertida != frase:
        print('A palavra digitada foi {} e o inverso dela é {}'.format(frase, frase_invertida))
        print('\033[1;31mNÃO É PALINDROMO\033[m')


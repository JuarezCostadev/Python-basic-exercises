from time import sleep
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Insira o peso da {}° pessoa: '.format(i)))
    sleep(0.5)
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if  peso < menor:
            menor = peso
else: 
    print('O maior peso lido foi de {}'.format(maior))
    print('O menor peso lido foi de {}'.format(menor))



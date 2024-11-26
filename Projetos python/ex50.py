soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Insira um valor: '))
    if num % 2 == 0:    
        soma += num
        cont += 1
print('VOCÊ INFORMOU {} e a soma dos números pares deu {}'.format(cont, soma))
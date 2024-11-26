n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(n1 , n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(n2, n1))
elif n1 == n2:
    print('Não tem maior, são iguais')
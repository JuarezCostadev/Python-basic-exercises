import random

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str (input('Insira o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)

print('O aluno(a) escolhido foi {}'. format(sorteio))
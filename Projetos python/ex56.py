somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '

for i in range(1, 5):
    print('--- {}° PESSOA ---'.format(i))
    nome = str(input('NOME: '.format(i))).strip()
    idade = int(input('IDADE: '.format(i)))
    sexo = str(input('SEXO (M/F) '.format(i))).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome



mediaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho, maioridadehomem))

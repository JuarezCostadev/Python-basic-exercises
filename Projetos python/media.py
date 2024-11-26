nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if (media) >= 5:
    print('A média do aluno foi {} com isso foi aprovado!'.format(media))
else:
    print("REPROVADO")
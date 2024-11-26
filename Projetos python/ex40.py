print('Bem-Vindo aluno!')
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {:.2f} e você foi REPROVADO'.format(media))
elif media > 5 and media < 7 :
    print('Suas notas foram {} e {} e a media foi {} Com isso está de recuperação!'.format(n1, n2, media))
elif media >= 7:
    print('PARABÉNS VOCÊ FOI APROVADO! com uma média de {} '.format(media))







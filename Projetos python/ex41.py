from datetime import date
#ENTRADA DE DADOS
nascimento = int(input('Insira o ano que nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
#CONDICIONAL
if idade <= 9:
    print('A sua idade é {} anos e sua categoria é a MIRIM'.format(idade))
elif idade > 9 and idade <=14:
    print('A sua idade é { } anos e sua categoria é a INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('A sua idade é {} anos e sua categoria é a JÚNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('A sua idade {} anos e sua categoria é SÊNIOR'.format(idade))
else:
    print('A sua idade é {} anos e sua categoria é MASTER'.format(idade))


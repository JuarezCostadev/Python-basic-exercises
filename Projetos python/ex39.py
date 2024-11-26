from datetime import date
#ENTRADA DE DADOS
nascimento = int(input('\033[7mInsira o seu ano de nascimento:\033[m '))
ano_atual = date.today().year
idade = ano_atual - nascimento
#MENOR DE 18 ANOS
if idade < 18:
    print('Você nasceu em {} e tem {} anos e deve se alistar em {}'.format(nascimento, idade, nascimento + 18))
    print('Faltam {} ano(s) para se alistar'.format(18 - idade))
#JÁ TEM 18 ANOS
elif idade == 18:
    print('\033[1;31;40mCompareça IMEDIATAMENTE a junta militar!!!\033[m')
#MAIORES DE 18 ANOS
elif idade >= 18:
    print('Vocé nasceu em {} e tem {} e deveria ter se alistado em {}'.format(nascimento, idade, nascimento + 18))
    print('Era para ter se alistado à {} anos'.format(idade - 18))







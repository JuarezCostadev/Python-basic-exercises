#ENTRADA DE DADOS
valor = float(input('Insira o valor do produto (R$): '))
print('''Insira a forma de pagamento desejada:
[ 1 ] À VISTA/ CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] EM ATE 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opçao = int(input('Insira a opção desejada '))
#CONDIÇAO
if opçao == 1:
    print('O valor do produto é R$ {} e com 10% de desconto fica R$ {:.2f}'.format(valor, valor - (valor * 0.10)))
elif opçao == 2:
    print('O valor do produto é R$ {} e com 5% de desconto fica R$ {:.2f}'.format(valor, valor - (valor * 0.05)))
elif opçao == 3:
    print('O valor do produto é R$ {} e não sofreu nenhuma mudança!'.format(valor))
elif opçao == 4:
    print('O valor do produto é R$ {} e com 20% de juros fica R$ {:.2f}'.format(valor, valor + (valor * 0.20)))
valor = float(input('Digite o valor do produto R$: '))
vd = valor * 0.05
vf = valor - vd

print("O valor inserido foi R$ {} com desconto ficou R$ {}".format(valor, vf))
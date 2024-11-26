n = int(input('Insira um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('\n MILHAR {} \n CENTENA {} \n DEZENA {} \n UNIDADE {} \n '.format(m, c, d, u))

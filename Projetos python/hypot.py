from math import hypot
num1 = float(input('Insira o valor do cateto oposto: '))
num2 = float(input('Insira o valor do cateto adjacente: '))
func = hypot(num1,num2)
print('A hipotenusa vai medir {:.2f}'.format(func))
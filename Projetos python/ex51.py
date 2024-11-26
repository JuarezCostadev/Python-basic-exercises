print('==' * 30)

print('10 TERMOS DE UMA P.A')

razao = int(input('Insira a razão da P.A: '))
termo = int(input('Insira o termo da P.A: '))

for c in range(termo, 11, razao):   
    print(c, end = ' ')
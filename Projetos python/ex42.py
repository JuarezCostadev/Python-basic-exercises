r1 = int(input('Insira o primeiro segmento: '))
r2 = int(input('Insira o segundo segmento: '))
r3 = int(input('Insira o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um TRIÂNGULO!')
    if r1 == r2 and r1 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('\033[1;30;40mOs segmentos acima PODEM FORMAR um triângulo ESCALENO\033[m')
    else:
        print('OS SEGMENTOS FORMAM UM ISÓSCELES! ')
else:
    print('NENHUM DOS SEGMENTOS ACIMA FORMAM UM TRIÂNGULO!!')
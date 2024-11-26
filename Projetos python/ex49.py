num = int(input('Insira um número para ver sua tabuada: '))
print('\033[1;36mTABUADA\033[m')
print('-=' * 30)
for c in range(0,11):
    print('{} X {} = {}'.format(c, num, c * num))
print('-=' * 30)
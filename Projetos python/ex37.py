#INSERIR DADOS
num = int(input('Insira um número inteiro: '))
print('''Escolhas uma das bases para conversão:
[ 1 ] \033[1;34;40mBinário\033[m
[ 2 ] \033[1;33;40mOctal\033[m
[ 3 ] \033[1;36;40mHexadecimal\033[m''')
opçao = int(input('Insira sua opção: '))
#CONDIÇÃO
if opçao == 1: 
    print('{} convertido para \033[1;34;40mBINÁRIO\033[m é igual a {}'.format(num, bin(num)))
elif opçao == 2:
    print('{} convertido para \033[1;33;40mOCTAL\033[m é igual a {}'.format(num, oct(num)))  
elif opçao == 3:
    print('{} convertido para \033[1;36;40mHEXADECIMAL\033[m é igual a {}'.format(num, hex(num)))
else:
    print('\033[1;31;40mOPÇÃO NÃO ENCONTRADA\033[m')
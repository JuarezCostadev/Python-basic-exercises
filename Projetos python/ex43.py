altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))
imc = peso / (altura ** 2)
#CONDICIONAL
if imc < 18.5:
    print('Seu IMC foi de {:.2f} e você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC foi de {:.2f} e você está no PESO IDEAL!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC foi de {:.2f} e você está com SOBREPESO!'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC foi de {:.2f} e você está com OBESIDADE!'.format(imc))
else:
    print('ALERTA! SEU IMC FOI DE {:.2f} VOCÊ ESTÁ COM OBESIDADE MÓRBIDA'.format(imc))


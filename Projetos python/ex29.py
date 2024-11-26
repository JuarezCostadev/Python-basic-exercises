velcarro = float(input('Insira a velocidade do carro: '))
formula = (velcarro - 80) * 7
if velcarro > 80:
    print('VOCÊ FOI MULTADO POR KM ULTRAPASSADO, TOTAL DA MULTA R$ {}'.format(formula))
else:
    print('VOCÊ ESTÁ NO LIMITE PERMITIDO')
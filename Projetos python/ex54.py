from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = ano_atual - nasc
    if idade > 18:
        totmaior += 1
    else:
        totmenor += 1
print('TOTAL DE PESSOAS MAIORES DE IDADE {}'.format(totmaior))
print('TOTAL DE PESSOAS MENORES DE IDADE {}'.format(totmenor))

    
   
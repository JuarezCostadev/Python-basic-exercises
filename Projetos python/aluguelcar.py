dia = int(input('Quantos dias o carro ficou alugado?: '))
km = float(input('Quantos Km foi pecorridos?: '))
valor_final = (dia * 60) + (km * 0.15)
print('O carro ficou alugado por {} dia(s) e percorreu {}km e valor final do aluguel é R${}'.format(dia, km, valor_final))
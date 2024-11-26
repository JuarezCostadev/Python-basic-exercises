nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))

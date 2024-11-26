nome = str(input('Digite seu nome: ')).strip()
frase = nome.split()
primeiro_nome = frase[0]
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras!'.format(len(nome.replace(' ' , ''))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome, len(primeiro_nome)))

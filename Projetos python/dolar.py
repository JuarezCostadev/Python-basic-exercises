real = float(input('Digite o valor que possui em R$: ' ))
dolar = float(input('Digite a cotação do dolar atual $: '))
print("O usuário com R$ {} pode comprar {:.2f} em dolares".format(real, real / dolar))
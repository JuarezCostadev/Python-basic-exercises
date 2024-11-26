
vetor = []


for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)


dicionario = {}

for i in range(10):
    dicionario[i] = vetor[i] * 2


print("Vetor de números inteiros:", vetor)
print("Dicionário com o dobro de cada valor:", dicionario)

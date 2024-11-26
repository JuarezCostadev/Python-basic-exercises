import random
from time import sleep

opçao = print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Insira sua jogada: '))
print('JO!!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!')
sleep(1)
computador = random.randint(0, 2)
#COMPUTADOR JOGA PEDRA
if computador == 0:
    if jogador == 0:
        print('Jogador jogou PEDRA')
        print('Computador jogou PEDRA') 
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador jogo PAPEL')
        print('Computador jogou PEDRA')
        print('Jogador VENCEU!')
    elif jogador == 2:
        print('Jogador jogou TESOURA')
        print('Computador jogou PEDRA')
        print('COMPUTADOR VENCEU!')
#COMPUTADOR JOGA PAPEL
if computador == 1:
    if jogador == 1:
        print('Jogador jogou PAPEL')
        print('Computador jogou PAPEL')
        print('EMPATE!')
    elif jogador == 0:
        print('Jogador jogou PEDRA')
        print('Computador jogou PAPEL')
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('Jogador jogou TESOURA')
        print('Computador jogou PAPEL')
        print('JOGADOR VENCEU!')
#COMPUTADOR JOGA TESOURA
if computador == 2:
    if jogador == 2:
        print('Jogador jogou TESOURA')
        print('Computador jogou TESOURA')
        print('EMPATE!')
    elif jogador == 0:
        print('Jogador jogou PEDRA')
        print('Computador jogou TESOURA')
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('Jogador jogou PAPEL')
        print('Computador jogou TESOURA')
        print('COMPUTADOR VENCEU!')



        

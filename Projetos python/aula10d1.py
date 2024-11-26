import random

pc = random.randint(0, 5)
player = int(input('Pensei nesse número: '))
if player == pc:
    print('VOCÊ ACERTOU, PARABÉNS! O número sorteado foi {}'.format(pc))
else:
    print('VOCÊ PERDEU TENTE NOVAMENTE! O número sorteado foi {}'.format(pc))
    
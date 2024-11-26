from math import cos, sin, tan, radians
num = float(input('Insira um angulo: '))
c = cos(radians(num))
s = sin(radians(num))
t = tan(radians(num))
print('O angulo de {} graus tem como cosseno {:.2f} graus o seno {:.2f} graus e sua tangente {:.2f} graus'.format(num, c, s, t))


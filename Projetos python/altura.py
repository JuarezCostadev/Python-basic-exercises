alt = float(input('Insira a altura: '))
lar = float(input('Insira a largura: '))
area = lar * alt
tinta = area / 2

print("Para pintar uma parede {}x{} é necessario {}L de tinta".format(lar, alt, tinta))    
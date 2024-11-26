from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;31mKABOMMMM\033[m')
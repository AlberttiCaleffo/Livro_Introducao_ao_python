numero = int(input('Numero: '))
contador_de_quebra = 0

while numero >= 2:
    if numero == 2 or numero == 3 or numero == 5 or\
        numero == 7:
        print(f'\033[1;32m{numero:<3}\033[1;32m', end= ' ')
    elif numero % 2 == 0 or numero % 3 == 0 or\
        numero % 5 == 0 or numero % 7 == 0:
        print(f'\033[1;31m{numero:<3}\033[1;31m', end= ' ')
    else:
        print(f'\033[1;32m{numero:<3}\033[1;32m', end= ' ')
    contador_de_quebra += 1
    numero -= 1
    if contador_de_quebra == 10:
        print()
        contador_de_quebra = 0
print('\033[37m\033[37m')
numero = int(input('Numero: '))
contador = 0

while contador <= 10:
    print(f'{numero} x {contador:<2} = {numero * contador:<2}')
    contador += 1
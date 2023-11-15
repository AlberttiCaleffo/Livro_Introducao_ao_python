numero = int(input('Numero: '))
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))

while inicio <= fim:
    print(f'{numero} x {inicio:<2} = {numero * inicio:<2}')
    inicio += 1
dividendo = int(input('1° Numero: '))
divisor = int(input('2° Numero: '))
quociente = 0

while True:
    if dividendo < divisor:
        dividendo = str(dividendo)
        dividendo += '0'
        dividendo = int(dividendo)
        quociente = float(quociente)
    else: 
        dividendo -= divisor
        if type(quociente) == float:
            quociente += 0.1
        else:
            quociente += 1
    if dividendo == 0:
        break

    
print(f'O resultado de {dividendo} dividido por {divisor} é {quociente}')
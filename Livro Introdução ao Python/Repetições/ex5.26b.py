dividendo = int(input('1° Numero: '))
divisor = int(input('2° Numero: '))
quociente = 0

while True:
    dividendo -= divisor
    quociente += 1
    if dividendo < divisor or dividendo == 0:
        break
    
print(f'O resultado de {dividendo} dividido por {divisor} é {quociente} inteiro.')
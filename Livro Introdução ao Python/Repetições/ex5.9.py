numero_1 = int(input('Primeiro numero: '))
numero_2 = int(input('Segundo numero: '))
quociente = 0
maior = numero_1 if numero_1 > numero_2 else numero_2
menor = numero_1 if numero_1 < numero_2 else numero_2
dividido = maior

while dividido >= menor:
    if numero_1 > numero_2:
        dividido -= numero_2
        quociente += 1
    else:
        dividido -= numero_1
        quociente += 1
print(quociente)
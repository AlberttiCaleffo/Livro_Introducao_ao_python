soma_numeros = media = 0

while True:
    numeros_inteiros = int(input('Numero inteiro: '))
    if numeros_inteiros == 0:
        break
    soma_numeros += numeros_inteiros
    media += 1
    
print(f'A soma de todos os numeros é {soma_numeros}\n'
      f'A media é {soma_numeros / media:.2f}')
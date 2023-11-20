while True:
    numero = input('Numero: ')
    if numero == numero[::-1]:
        print(f'O numero {numero} é palindromo!')
    else:
        print(f'O numero {numero} não é palindromo.')
    if numero == 0:
        break 
numero = int(input('Informe um numero: '))
tabuada = 1

while True:
    print(
        'Menu:\n'
        '1 - Subtração\n'
        '2 - Divisão\n'
        '3 - Multiplicação\n'
        '4 - Adição\n'
        '5 - Sair\n'
          )
    escolha_usuario = input('Qual das opções? ').lower().strip()
    print()
    if escolha_usuario == '1' or 'sub' in escolha_usuario:
        while tabuada <= 10:
            print(f'{numero} - {tabuada} = {numero - tabuada}')
            tabuada += 1
    elif escolha_usuario == '2' or 'div' in escolha_usuario:
        while tabuada <= 10:
            print(f'{numero} \ {tabuada} = {numero / tabuada:.2f}')
            tabuada += 1
    elif escolha_usuario == '3' or 'mult' in escolha_usuario:
        while tabuada <= 10:
            print(f'{numero} * {tabuada} = {numero * tabuada}')
            tabuada += 1
    elif escolha_usuario == '4' or 'adi' in escolha_usuario:
        while tabuada <= 10:
            print(f'{numero} + {tabuada} = {numero + tabuada}')
            tabuada += 1
    elif escolha_usuario == '5' or 'sair' in escolha_usuario:
        break
    else:
        print('Valor invalido...')
    print()
    tabuada = 1
    numero = int(input('Insira outro valor: '))
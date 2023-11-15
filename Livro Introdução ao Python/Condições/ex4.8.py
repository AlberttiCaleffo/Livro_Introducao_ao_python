primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
operacao = input('Qual operação?\n'
                 'Soma [+]\n'
                 'Subtração [-]\n'
                 'Divisão [/]\n'
                 'Multiplicação [*]\n'
                 '> ')

if '+' in operacao:
    print(f'{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}')
elif '-' in operacao:
    print(f'{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}')
elif '*' in operacao:
    print(f'{primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero}')
elif '/' in operacao:
    print(f'{primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero}')
else:
    print('Valor invalido.')
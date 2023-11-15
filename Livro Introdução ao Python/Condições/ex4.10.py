kWh = int(input('Quantos kWh consumidos? '))
tipo_de_instalacao = input('Tipo de instalação:\n'
                           'Residencial [R]\n'
                           'Comercial [C]\n'
                           'Industrial [I]\n'
                           '> ').upper().strip()

if tipo_de_instalacao == 'R':
    if kWh <= 500:
        print(f'A pagar: R${kWh * 0.40:.2f}')
    else:
        print(f'A pagar: R${kWh * 0.65:.2f}')
elif tipo_de_instalacao == 'C':
    if kWh <= 1000:
        print(f'A pagar: R${kWh * 0.55:.2f}')
    else:
        print(f'A pagar: R${kWh * 0.60:.2f}')
elif tipo_de_instalacao == 'I':
    if kWh <= 5000:
        print(f'A pagar: R${kWh * 0.55:.2f}')
    else:
        print(f'A pagar: R${kWh * 0.60:.2f}')
else:
    print('Valor invalido.')
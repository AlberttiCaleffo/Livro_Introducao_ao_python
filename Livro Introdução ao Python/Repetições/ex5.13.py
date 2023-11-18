divida = float(input('Quantia da dívida: '))
juros_mensal = float(input('Juros mensais: '))
pago_mensalmente = float(input('Pagamento mensal: '))
meses_pagando = 1
quantia_paga = 0

print(f'Valor pago por mês: {pago_mensalmente}')
while divida != 0:
    if divida < pago_mensalmente:
        quantia_paga += divida
        divida = 0
        continue
    print(f'Mês {meses_pagando}')
    divida += divida * juros_mensal / 100
    divida -= pago_mensalmente
    quantia_paga += pago_mensalmente
    print(f'Divida: {divida:.2f}')
    print('-=' * 10)
    meses_pagando += 1
print(f'Total pago: {quantia_paga:.2f}')
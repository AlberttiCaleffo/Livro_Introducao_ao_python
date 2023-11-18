deposito_inicial = float(input('Quantia: '))
juros_poupanca = float(input('Juros da poupança: '))
contador = 1

while contador <= 24:
    ganhos_poupanca = deposito_inicial * juros_poupanca / 100
    print(f'Mês {contador}: {ganhos_poupanca:.2f}')
    deposito_inicial += ganhos_poupanca
    contador += 1
print(f'Acumulado em 24 meses: {deposito_inicial:.2f}')
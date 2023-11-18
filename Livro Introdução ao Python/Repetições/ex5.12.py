deposito_inicial = float(input('Quantia inicial: '))
deposito_mensal = float(input('Quantia mensal: '))
juros_poupanca = float(input('Juros da poupança: '))
contador = 1
acumulado = total_bruto = deposito_inicial
juros_total = 0

while contador <= 24:
    ganhos_poupanca = acumulado * juros_poupanca / 100
    print(f'Mês {contador}: {ganhos_poupanca:.2f}')
    acumulado += ganhos_poupanca
    acumulado += deposito_mensal
    juros_total += ganhos_poupanca
    total_bruto += deposito_mensal
    contador += 1

print('-=' * 10)    
print(f'Valor bruto: {total_bruto}\n'
      f'Juros obtido: {juros_total:.2f}\n'
      f'Acumulado em 24 meses: {acumulado:.2f}')
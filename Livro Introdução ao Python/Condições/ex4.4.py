salario = float(input('Qual o seu salario: '))

if salario > 1250:
    print(f'{salario * 0.10 + salario}')
if salario <= 1250:
    print(f'{salario * 0.15 + salario}')
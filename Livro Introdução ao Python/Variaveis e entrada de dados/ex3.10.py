salario = float(input('Salario: '))
aumento = int(input('Aumento: %')) / 100

print(f'O aumento do salario é R$ {aumento * salario:.2f}. Com o aumento fica R$ {(salario * aumento) + salario:.2f}')
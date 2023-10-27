km = float(input('Quantos km a percorrer? '))

if km <= 200:
    print(f'A viagem vai ser cobrada por R$ {km * 0.50:.2f}')
else:
    print(f'A viagem vai ser cobrada por {km * 0.45:.2f}')
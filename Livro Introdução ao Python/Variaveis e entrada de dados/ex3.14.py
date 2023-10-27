percorrido = float(input('Quantos km percorrido o carro ja tem? '))
dias_alugado = int(input('Por quantos dias foi alugado? '))
valor_a_pagar = dias_alugado * 60 + 0.15 * percorrido

print(f'O carro foi alugado por {dias_alugado} dias e foi percorrido {percorrido}km.\n'
      f'O valor a pagar é R$ {valor_a_pagar:.2f}')
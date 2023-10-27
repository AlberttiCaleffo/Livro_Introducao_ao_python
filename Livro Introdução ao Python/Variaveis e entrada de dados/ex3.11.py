valor_produto = int(input('Qual o valor da mercadoria? '))
desconto = int(input('Qual o valor do desconto? '))
desconto_aplicado = desconto / 100 * valor_produto

print(f'O valor do produto R$ {valor_produto:.2f} com o desconto de {desconto}% fica em R$ {desconto_aplicado + valor_produto:.2f}')
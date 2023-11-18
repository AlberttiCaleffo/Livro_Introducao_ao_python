total_compras = 0

while True:
    codigo_produto = input('Codigo do produto: ')
    if codigo_produto == '1':
        print('O valor deste produto é 0,50')
        quantidade_comprada = int(input('Quantidade: '))
        total_compras += quantidade_comprada * 0.50
    elif codigo_produto == '2':
        print('O valor deste produto é 1,00')
        quantidade_comprada = int(input('Quantidade: '))
        total_compras += quantidade_comprada * 1.00
    elif codigo_produto == '3':
        print('O valor deste produto é 4,00')
        quantidade_comprada = int(input('Quantidade: '))
        total_compras += quantidade_comprada * 4.00
    elif codigo_produto == '4':
        print('O valor deste produto é 7,00')
        quantidade_comprada = int(input('Quantidade: '))
        total_compras += quantidade_comprada * 7.00
    elif codigo_produto == '5':
        print('O valor deste produto é 8,00')
        quantidade_comprada = int(input('Quantidade: '))
        total_compras += quantidade_comprada * 8.00
    elif codigo_produto == '0':
        break     
    else: 
        print('Valor invalido!')
print(f'O valor total da compra é R${total_compras:.2f}')
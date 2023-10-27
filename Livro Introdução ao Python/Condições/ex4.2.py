velocidade = float(input('Qual a velocidade do seu carro? '))

if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 5
    print(f'A multa é de R$ {multa:.2f}')
if velocidade <= 80:
    print('Dentro do permitido.')
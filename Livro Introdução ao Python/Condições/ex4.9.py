valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario: '))
anos_a_pagar = int(input('Quantos anos a pagar? '))
maior_30 = salario * 0.30
prestacao = valor_casa / (anos_a_pagar * 12)
prestacao_f = f'R${prestacao:,.2f}'.replace('.', ',').replace(',', '.', 1)
valor_casa_f = f'R${valor_casa:,.2f}'.replace('.', ',').replace(',', '.', 1)

if prestacao > maior_30:
    print(
        'Você não tem condições para ter um emprestimo...\n'\
        f'Valor da prestação ({prestacao_f}) menor que os 30% do salario (R${maior_30:.2f})\n'\
        'NEGADO!'
        )
else:
    print(
        f'O valor da casa é {valor_casa_f}.\n'\
        f'A prestação é {prestacao_f} em {anos_a_pagar} anos, menor que os 30% do salario (R${maior_30:.2f}).\n'\
         'APROVADO!'
            )
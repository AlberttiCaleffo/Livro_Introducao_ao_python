cigarros = int(input('Quantos cigarros por dia? '))
anos_fumando = int(input('Quantos anos fumando? '))
cigarro_fumados = cigarros * (365 * anos_fumando) * 10

print(f'Perdera {cigarro_fumados / 60 / 24:.0f} dias de vida.')
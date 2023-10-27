dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

segundos_totais = (((((dias * 24) + horas) * 60) + minutos) * 60) + segundos

print(f'{segundos_totais:,.0f} segundos'.replace(',', '.'))
abre_parenteses = []
errado = False
expressao = input('Digite a expressão: ')

for parentese in expressao:
    if '(' in parentese:
        abre_parenteses.append(parentese)
    if ')' in parentese and abre_parenteses == []:
        errado = True
        break
    if ')' in parentese:
        del abre_parenteses[-1]
        
if len(abre_parenteses) > 0 or errado:
    print('Incorreto')
else:
    print('Correto')
        
# if len(abre_parenteses) == len(fecha_parenteses):
#     print('Correto!')
# else:
#     print('Errado.')
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print(f'O {n1} é maior')
if n2 > n1 and n2 > n3:
    print(f'O {n2} é maior')
if n3 > n1 and n3 > n2:
    print(f'O {n3} é o maior')
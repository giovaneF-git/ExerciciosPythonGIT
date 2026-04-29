a = int(input('Informe o valor de A \n'))
b = int(input('Informe o valor de B \n'))
aux = b
if a != b:
    aux = a
    a = b
    b = aux
print(20*'x', 'Inversão Mágica', 20*'x')
print('A se tornou {} e B se tornou {}'.format(a, b))
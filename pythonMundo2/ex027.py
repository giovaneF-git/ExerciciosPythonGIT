print('*=' * 10 + ' Sequência Fibonacci ' + '=*' * 10)
cont = int(input('Informe quantos números da Sequência Fibonacci deseja verificar: '))
a = 0
b = 1
soma = 0
while cont > 0:
    print('{} -> '.format(a), end='')
    soma = a + b
    a = b
    b = soma
    cont -= 1
print('Fim!')
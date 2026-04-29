print('*' * 10 + ' Tabuada ' + '*' * 10)
num = float(input('Informe qual número deseja descobrir a tabuada \n'))
print('Adição')
for i in range(1, 11):
    resultadoAdi = num + i
    print('{} + {} = {}'.format(num, i, resultadoAdi))
print('*' * 20)
print('Subtração')
for i in range(1, 11):
    resultadoSub = num - i
    print('{} - {} = {}'.format(num, i, resultadoSub))
print('*' * 20)
print('Multiplicação')
for i in range(1, 11):
    resultadoMulti = num * i
    print('{} - {} = {}'.format(num, i, resultadoMulti))
print('*' * 20)
print('Divisão')
for i in range(1, 11):
    resultadoDivi = num / i
    print('{} / {} = {:.1f}'.format(num, i, resultadoDivi))
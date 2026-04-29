print('*' * 20 + ' Calculadora de Fatorial ' + '*' * 20)
num = int(input('Informe o número para descobrirmos seu fatorial: '))
vx = num
aux = 0
resultado = 1
for vx in range(vx, 0, -1):
    resultado *= vx
print('O fatorial {}! é {}'.format(num, resultado))
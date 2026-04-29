print('*' * 20 + ' Calculadora de Fatorial ' + '*' * 20)
num = int(input('Informe um número para descobrirmos seu fatorial: '))
vx = num
resultado = 1
while vx > 0:
    resultado *= vx
    print(vx, end='*')
    vx -= 1
print('\n O fatorial de {}! é {}'.format(num, resultado))
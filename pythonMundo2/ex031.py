print('*' * 10 + ' Tabuada de Multiplicação ' + '*' * 10)
print('Quando desejar encerrar, coloque um número negativo que o programa encerrará automaticamente.')
multi = 1
while True:
    n = int(input('Informe o número que deseja verificar a tabuada: '))
    if n < 0:
        break
    multi = 1
    while multi <= 10:
        print(f'{n} * {multi} = {n * multi}')
        multi += 1
print('Programa encerrado.')
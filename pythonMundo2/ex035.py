print('*' * 40)
print (' ' * 15 + 'Banco GF ')
print('*' * 40)
valor = int(input('Informe o valor que deseja sacar: '))
total = valor
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de cédulas: {totalCed} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print('Obrigado por utilizar nosso serviços. Volte sempre!')
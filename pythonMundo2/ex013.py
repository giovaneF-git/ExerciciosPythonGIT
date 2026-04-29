print('Você informará 6 números e descobrirá a soma somente dos números pares! ')
soma = 0
for i in range(0, 6):
    num = int(input('Informe o número '))
    if num % 2 == 0:
        soma += num
print('A soma dos pares é {}'.format(soma))
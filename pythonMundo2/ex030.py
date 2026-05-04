print('*-' * 10)
print(' Somas Aleatórias ')
print('-*' * 10)
rep = soma = 0
n = int(input('Informe o primeiro número: '))
while True:
    soma += n
    n = int(input('Próximo número (Para encerrar, digite 999) \n'))
    rep += 1
    if n == 999:
        break
print(f'Você adicionou {rep} números e o somatório total é {soma}.')
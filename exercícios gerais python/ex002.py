menor = 0
medio = 0
maior = 0
print(20*'*', ' Organizador de números em ordem crescente ', 20*'*')
for i in range(1,4):
    num = int(input('Informe o {}º número \n'.format(i)))
    if i == 1:
        menor = num
        medio = num
        maior = num
    else:
        if menor > num:
            menor = num
        elif maior < num:
            maior = num
        else:
            medio = num
print('A ordem crescente é: {} -> {} -> {}'.format(maior,medio,menor))
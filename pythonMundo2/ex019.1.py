maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('informe o peso da {}º pessoa '.format(p)))
    if p == 1:
        menor = medio = maior = num
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O maior peso registrado é {} e o menor peso registrado é {}'.format(maior, menor))
menorPeso = 1000
maiorPeso = 0
for i in range(0, 5):
    peso = float(input('Informe seu peso \n'))
    if peso < menorPeso:
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso;
print('O maior peso é {}Kgs e o menor peso é {}Kgs'.format(maiorPeso, menorPeso))
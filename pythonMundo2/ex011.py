soma = 0
cont = 0
for i in range (0, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        cont = cont + 1
print('Soma de todos os valores "{}" é {}'.format(cont, soma))
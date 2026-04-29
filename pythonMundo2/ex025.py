print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
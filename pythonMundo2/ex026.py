print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Informe a primeira PA: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 10
quantosTermos = 0
while cont > 0:
    print('{} -> '.format(termo), end='')
    cont -= 1
    termo += razao
    quantosTermos += 1
    if cont == 0:
        print('Pausa')
        continuacao = int(input('Deseja mostrar mais quantos termos? (Digite 0 para encerrar o programa) '))
        cont = continuacao
print('Progressão finalizada com {} termos.'.format(quantosTermos))
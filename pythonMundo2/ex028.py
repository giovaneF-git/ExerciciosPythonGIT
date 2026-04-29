print('-=' * 20)
print(' ' * 10 + ' Somas Aleatórias ' + ' ' * 10)
print('-=' * 20)
somatorio = 0
rep = 0
n = int(input('Informe números para somar, quando decidir verificar o valor total, basta apenas digitar 999! \n'))
while n != 999:
    somatorio += n
    n = int(input('Digite mais um valor!: '))
    rep += 1
print('A soma total é "{}" e você adicionou números {} vezes!'.format(somatorio, rep))
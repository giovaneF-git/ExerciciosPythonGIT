num = 0
c = 1
print('Você infomará um valor por vez, quando desejar realizar a soma, basta colocar 0 para ter o resultado')
while c != 0:
    c = int(input('Informe o valor, 0 para realizar soma \n'))
    num += c
print('O resultado de é {}'.format(num))
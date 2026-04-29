n = int(input('Informe o primeiro número inteiro \n'))
n2 = int(input('Informe o segundo número inteiro \n'))
if n > n2:
    print('O primeiro número inteiro ({}) é maior que o segundo número inteiro ({})'.format(n, n2))
elif n2 > n:
    print('O segundo número inteiro ({}) é maior que o primeiro número inteiro ({})'.format(n2, n))
else:
    print('Os números são iguais')
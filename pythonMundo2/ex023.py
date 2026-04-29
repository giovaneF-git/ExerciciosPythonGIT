a = float(input('Informe o primeiro valor: '))
b = float(input('Informe o segundo valor: '))
escolha = 0
c = 0
while escolha != 5:
    escolha = int(input('[1] para Somar \n'+
                        '[2] para Subtrair \n' +
                        '[3] para Multiplicar \n'+
                        '[4] para Dividir \n' +
                        '[5] para Sair do Programa \n'))
    if escolha == 1:
        c = a + b
        print(f'O resultado da soma é: {c}')
    elif escolha == 2:
        c = a - b
        print(f'O resultado da subtração é: {c}')
    elif escolha == 3:
        c = a * b
        print(f'O resultado da multiplicação é: {c}')
    elif escolha == 4:
        c = a / b
        print(f'O resultado da divisão é: {c:.2f}')
print('*'*5 + ' Programa Encerrado ' + '*' * 5)
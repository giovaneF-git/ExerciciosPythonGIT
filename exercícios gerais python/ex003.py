aumento = 0
percentual = 0
percentualTextil = ''
salarioAtualizado = 0
novoSalario = 0
aumento = 0
print('*'*20, ' Calculadora de Ajustes Salariais ', 20*'*')
for i in range(0,3):
    salario = float(input('Informe seu salário para verificarmos o aumento \n'))
    if salario < 281:
        percentual = 0.2
        percentualTextil = '20%'
    elif salario < 701:
        percentual = 0.15
        percentualTextil = '15%'
    elif salario < 1501:
        percentual = 0.1
        percentualTextil = '10%'
    else:
        percentual = 0.05
        percentualTextil = '5%'
    aumento = salario * percentual
    novoSalario = salario + aumento
    print('Com o salário de R${}, você receberá um aumento de {}, equivalente a R${:.2f}. Seu novo salário ajustado será R${}'.format(salario, percentualTextil, aumento, novoSalario))
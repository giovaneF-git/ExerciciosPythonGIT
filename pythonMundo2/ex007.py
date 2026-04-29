print('*'*20, ' Calculadora de IMC ', '*'*20)
altura = float(input('Informe sua altura \n'))
peso = float(input('Informe seu peso \n'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso, seu IMC está {:.1f}.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal, seu IMC está {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está acima do peso, seu IMC está {:.1f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Você está com obesidade, seu IMC está {:.1f}'.format(imc))
elif imc >= 40:
    print('Você está com obesidade mórbida, seu IMC está {:.1f}'.format(imc))
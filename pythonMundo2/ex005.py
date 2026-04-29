nome = input('Informe o nome do competidor \n')
idade = int(input('Informe a idade do competir para alocarmos na subdivisão \n'))
if idade <= 9:
    print('O competidor {} será alocado na subdivisão mirim!'.format(nome))
elif idade >= 10 and idade <= 14:
    print('O competidor {} será alocado na subdivisão infantil!'.format(nome))
elif idade >= 15 and idade <= 19:
    print('O competidor {} será alocado na subdivisão junior!'.format(nome))
elif idade == 20:
    print('O competidor {} será alocado na subdivisão sênior!'.format(nome))
else:
    print('O competidor {} será alocado na subdivisão master!'.format(nome))
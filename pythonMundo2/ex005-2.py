from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento \n'))
idade = atual - nascimento
if idade <= 9:
    print('Com idade {}, será alocado na subdivisão mirim!'.format(idade))
elif idade <= 14:
    print('Com idade {}, será alocado na subdivisão infantil!'.format(idade))
elif idade <= 19:
    print('Com idade {}, será alocado na subdivisão junior!'.format(idade))
elif idade == 20:
    print('Com idade {}, será alocado na subdivisão sênior!'.format(idade))
else:
    print('Com idade {}, será alocado na subdivisão master!'.format(idade))
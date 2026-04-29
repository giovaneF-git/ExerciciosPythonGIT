from datetime import date
atual = date.today().year
nasc = int(input('Informe seu ano de nascimento \n'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você está no tempo correto para se alistar')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda faltam {} anos para você se alistar.'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Você já está atrasado para o alistamento há {} anos.'.format(abs(tempo)))
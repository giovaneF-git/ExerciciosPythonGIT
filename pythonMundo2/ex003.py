nome = input('Informe seu nome completo \n')
anoNascimento = int(input('Informe seu ano de nascimento \n'))
idadeAlistamento = 2026 - anoNascimento
if idadeAlistamento < 18:
    idade = idadeAlistamento - 18
    print('Você não pode se alistar agora, pois faltam {} anos para você completar a idade mínima'.format(abs(idade)))
elif idadeAlistamento == 18:
    print('Você está na idade correta para se alistar')
elif idadeAlistamento > 18:
    idade = idadeAlistamento - 18
    print('Você já está atrasado para o alistamento há {} anos, por favor, realize o alistamento já.'.format(idade))
g = ''
nome = input('Por favor, informe seu nome \n')
while g != 'M' and g != 'H':
    g = input('Agora, informe seu gênero, com H para Homem e M para Mulher. \n').upper()
    if g != 'M' and g != 'H':
        print('Tente novamente com os caracteres corretos, "H" para Homem e "M" para mulher')
if g == 'H':
    print('Olá {}, seja bem-vindo!'.format(nome))
if g == 'M':
    print('Olá {}, seja bem-vinda!'.format(nome))
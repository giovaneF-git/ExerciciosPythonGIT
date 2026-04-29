nome = input('Informe seu nome \n')
if nome == 'Giovane':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('seu nome é bem comum..')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Nome belíssimo')
else:
    print('Olá!')
print('Bom dia, seja bem-vindo {}!'.format(nome))

nome = input('Informe o nome completo do aluno \n')
nota1 = float(input('Informe a primeira nota do aluno \n'))
nota2 = float(input('Informe a segunda nota do aluno \n'))
nota3 = float(input('Informe a terceira nota do aluno \n'))
media = (nota1 + nota2 + nota3) / 3
if media <= 4.9:
    print('O aluno {} foi reprovado por média {:.2f}'.format(nome, media))
elif media >= 5 and media <= 6.9:
    print('O aluno {} está em recuperação pela média {:.2f}'.format(nome, media))
else:
    print('Parabéns {}, você foi aprovado diretamente!'.format(nome))
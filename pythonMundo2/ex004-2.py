nota1 = float(input('Informe a primeira nota do aluno \n'))
nota2 = float(input('Informe a segunda nota do aluno \n'))
nota3 = float(input('Informe a terceira nota do aluno \n'))
media = (nota1 + nota2 + nota3) / 3
if 7 > media >= 5:
    print('Você está em recuperação')
elif media > 7:
    print('Parabéns, você está aprovado')
elif media <5:
    print('Você está reprovado, sem direito a recuperação')
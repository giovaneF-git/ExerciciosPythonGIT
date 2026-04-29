anoAtual = 2026
maiorIdade = 0
menorIdade = 0
for i in range(1, 8, 1):
    anoNascimento = int(input('Informe o ano de nascimento \n'))
    idade = anoAtual - anoNascimento
    if idade == 18 or idade > 18:
        maiorIdade = maiorIdade +1
    else:
        menorIdade = menorIdade + 1
print('{} já atingiram a maioridade e {} ainda não atingiram a maioridade'.format(maiorIdade,menorIdade))
print('=-' * 10 + ' Cadastro de Gênero e idade anônimo ' + '-=' * 10)
maiorIdade = homens = mulheres = mulheresMenores = 0
while True:
    genero = input('M para masculino e F para feminino: ').upper()
    idade = int(input('Informe a idade: '))
    if genero == 'M':
        homens += 1
    if genero == 'F':
        mulheres += 1
    if idade > 18:
        maiorIdade += 1
    if genero == 'F' and idade < 20:
        mulheresMenores += 1
    continuar = input('Deseja continuar? S para continuar ou N para finalizar o programa. ').upper()
    if continuar == 'N':
        break
print('=--=' * 10)
print(f'Maiores de 18 anos registrados: {maiorIdade} \n'
      f'Homens registrados {homens}: \n'
      f'Mulheres com menos de 20 anos registradas {mulheresMenores}')
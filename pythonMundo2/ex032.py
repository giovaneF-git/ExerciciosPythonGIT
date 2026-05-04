from random import randint
print('*' * 40)
print(' ' * 10 + ' Par ou Ímpar! ')
print('*' * 40)
vitorias = computador = soma = par = impar = 0
while True:
    computador = randint(0,10)
    n = int(input('Digite entre 0 e 10: '))
    escolha = input('Você deseja Par ou Ímpar? Digite P para Par ou I Para Ímpar: ').upper()
    soma = computador + n
    if soma % 2 == 0:
        par = 1
    else:
        impar = 1
    print(f'O computador escolheu: {computador}')
    if escolha == 'P' and par == 1:
        vitorias += 1
    elif escolha == 'I' and impar == 1:
        vitorias +=1
    else:
        break
    impar = par = 0
print(f'Você venceu {vitorias} vezes!')
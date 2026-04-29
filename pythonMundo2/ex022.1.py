from random import randint
computador = randint(1,10)
print('*' * 20 + ' Jogo da adivinhação ' + '*' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Faça sua tentativa! "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente novamente.. um pouco mais pra cima ')
        elif jogador > computador:
            print('Tente de novo.. um pouco mais pra baixo')
print('Você acertou! \n')
print('Precisou apenas de {} palpites.. '.format(palpites))
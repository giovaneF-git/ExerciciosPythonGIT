import random
print('*'*20, 'Vamos jogar e garanta um prêmio!', '*'*20)
jogador = input('Você quer jogar pedra, papel ou tesoura? \n')
computador = ['pedra','papel','tesoura']
escolhaComputador = random.choice(computador)
print('computador: {}'.format(escolhaComputador))
if jogador == 'pedra' and escolhaComputador == 'tesoura':
    print('Parabéns, você escolheu {} e o computador jogou {}, então você ganhou!'.format(jogador, escolhaComputador))
elif jogador == 'pedra' and escolhaComputador == 'papel':
    print('O computador ganhou! Você escolheu {} e o computador jogou {}'.format(jogador, escolhaComputador))
elif jogador == 'tesoura' and escolhaComputador == 'papel':
    print('Parabéns, você escolheu {} e o computador jogou {}, então você ganhou!'.format(jogador, escolhaComputador))
elif jogador == 'tesoura' and escolhaComputador == 'pedra':
    print('O computador ganhou! Você escolheu {} e o computador jogou {}'.format(jogador, escolhaComputador))
elif jogador == 'papel' and escolhaComputador == 'pedra':
    print('Parabéns, você escolheu {} e o computador jogou {}, então você ganhou!'.format(jogador, escolhaComputador))
elif jogador =='papel' and escolhaComputador == 'tesoura':
    print('O computador ganhou! Você escolheu {} e o computador jogou {}'.format(jogador, escolhaComputador))
else:
    print('Você jogou {} e o computador {}, então empataram!'.format(jogador,escolhaComputador))
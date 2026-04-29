from random import randint
palpite = 0
num = 0
sorteado = randint(1, 10)
while num != sorteado:
    num = int(input('Informe o número para descobrir qual foi sorteado: '))
    palpite += 1
print("Você precisou de {} palpites, o número sorteado foi {}".format(palpite, sorteado))
if palpite < 3:
    print('Parabéns, você conseguiu acertar com menos de 3 tentativas, você receberá o prêmio de R$1000')
elif palpite < 6:
    print('Com menos de 5 tentativas, você receberá o prêmio de R$100')
else:
    print('Com tantas tentativas, você não poderá receber nenhum prêmio :(')
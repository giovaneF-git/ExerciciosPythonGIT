idadeHomem = 0
nomeMaisVelho = ''
idadeSoma = 0
mulherMaisNova = 0
for i in range(0,4):
    nome = input('Informe seu nome \n')
    genero = input('Informe M para masculino ou F pra feminino \n')
    idade = int(input('Informe quantos anos você tem \n'))
    idadeSoma += idade
    if genero == 'M' and idade > idadeHomem:
        nomeMaisVelho = nome
    if genero == 'F' and idade < 20:
        mulherMaisNova = mulherMaisNova + 1
idadeMedia = idadeSoma / 4
print('A idade média das 4 pessoas é {}, o nome do homem mais velho é {} e {} são mulheres com menos de 20 anos'.format(idadeMedia, nomeMaisVelho, mulherMaisNova ))
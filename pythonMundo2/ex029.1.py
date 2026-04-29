print('*' * 20)
print(' ' * 10 + ' Calculadora de Média Infinita ' + ' ' * 20)
print('*' * 20)
n = float(input('Informe o primeiro número para descobrir a média: '))
somatorio = rep = menor = maior = 0
continuar = ''
while continuar not in ['NAO', 'NÃO', 'N']:
    n = float(input('Informe mais um número: '))
    somatorio += n
    rep += 1
    if rep == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Deseja adicionar mais um número? ').upper()
media = somatorio / rep
print(f'A média dos números digitados é: {media:.2f}, o maior número digitado foi {maior} e o menor {menor}')
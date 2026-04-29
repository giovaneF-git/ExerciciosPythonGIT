print('=' * 20)
print('Dez termos de uma PA')
print('=' * 20)
primeiroTermo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termos = int(input('Informe a quantidas: '))
formulaTermos = primeiroTermo + (termos - 1) * razao
for i in range(primeiroTermo, formulaTermos, razao):
    print('{} '.format(i), end = '-> ')
print('Finalizado!')

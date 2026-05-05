print('-' * 40)
print(' ' * 10 + ' Lista de Compras ' + ' ' * 10)
print('-' * 40)
produtos = valorTotal = menorValor = produtosMaisCaros = 0
produtoMaisBarato = ''
while True:
    nomeProduto = input('Informe o nome do produto: ')
    valorProduto = float(input('Informe o valor do produto: '))
    produtos += 1
    valorTotal += valorProduto
    if produtos == 1:
        menorValor = valorProduto
    else:
        if valorProduto < menorValor:
            menorValor = valorProduto
            produtoMaisBarato = nomeProduto
    if valorProduto >= 1000:
        produtosMaisCaros += 1
    continuar = input('Deseja continuar cadastrando produtos na lista de compras? S/N: ').upper()
    if continuar == 'N':
        break
print(f'Total gasto {valorTotal:.2f} \n'
      f'Quantidade de produtos que custaram mais de R$1000: {produtosMaisCaros} \n'
      f'Produto mais barato: {produtoMaisBarato} e custou {menorValor}')
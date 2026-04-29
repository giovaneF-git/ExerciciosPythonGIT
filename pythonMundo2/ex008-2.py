print('*'*20, ' Calculadora de preço final ','*'*20 )
preco = float(input('Informe o valor original do produto \n'))
formaPagamento = input('Informe a forma de pagamento \n')
if formaPagamento in 'Dinheiro dinheiro cheque Cheque':
    precoFinal = preco - (preco * 0.1)
    print('O cliente receberá 10% de desconto, pagando apenas R${:.2f}'.format(precoFinal))
elif formaPagamento == 'Cartão' or formaPagamento == 'cartão':
    precoFinal = preco - (preco * 0.05)
    print('O cliente receberá 5% de desconto, pagando apenas R${:.2f}'.format(precoFinal))
elif formaPagamento == '2x':
    parcela = preco / 2
    print('O cliente pagará o valor de R${:.2f} em duas parcelas de R${:.2f}'.format(preco, parcela))
elif formaPagamento == '3x':
    precoFinal = preco + (preco * 0.2)
    parcela = precoFinal / 3
    print('O cliente pagará o valor de R${:.2f}, em três parcelas de R${:.2f}'.format(precoFinal, parcela))
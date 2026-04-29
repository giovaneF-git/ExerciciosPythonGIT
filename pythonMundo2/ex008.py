print('*'*20, 'Calculadora de preço final', '*'*20)
preco = float(input('Informe o preço original do produto \n'))
formaPagamento = int(input('Informe a forma de pagamento: \n'
                             '1 para Dinheiro ou Cheque à vista \n'
                             '2 para Cartão à vista \n'
                           '3 para Parcelado em 2x no Cartão \n'
                           '4 para Parcelado em 3x no Cartão \n'))
if formaPagamento == 1:
    precoFinal = preco - (preco * 0.1)
    print('O cliente receberá 10% de desconto, pagando R${:.2f}'.format(precoFinal))
elif formaPagamento == 2:
    precoFinal = preco - (preco * 0.05)
    print('O cliente receberá 5% de desconto, pagando R${:.2f}'.format(precoFinal))
elif formaPagamento == 3:
    parcela = preco / 2
    print('O cliente pagará {:.2f}, com duas parcelas de R${:.2f}'.format(preco, parcela))
elif formaPagamento == 4:
    precoFinal = preco + (preco * 0.2)
    parcela = precoFinal / 3
    print('O cliente pagará {:.2f}, com três parcelas de R${:.2f}'.format(precoFinal, parcela))
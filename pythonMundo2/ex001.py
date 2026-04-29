valorCasa = float(input('Informe o valor da casa que comprar \n'))
salario = float(input('Agora, informe o valor de seu salário mensal \n'))
pagamentoAnos = float(input('Informe em quantos anos deseja realizar o pagamento do empréstimo \n'))
mensalidade = valorCasa / (pagamentoAnos * 12)
if mensalidade <= salario * 0.3:
    print('Parabéns, seu empréstimo será liberado, pois a mensalidade ficará em parcelas de {:.2f}'.format(mensalidade))
else:
    print('A mensalidade ultrapassa o percentual permitido referente a 30% do seu salário, ficando {:.2f}'.format(mensalidade))
a = float(input('Informe o lado a do triângulo \n'))
b = float(input('Infomorme o lado b do triângulo \n'))
c = float(input('Informe o lado c do triângulo \n'))
if a == b == c:
    print('O triângulo apresenta todos os lados em medidas iguais, então é um equilátero ')
elif a == b or a == c or b == c:
    print('O triângulo apresenta dois lados iguais e um diferente, então é um isósceles ')
elif a != b != c:
    print('O triângulo apresenta todos os lados com medidas diferentes, então é um escaleno ')
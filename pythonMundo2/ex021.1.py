sexo = input('Informe seu gênero com M ou F: ').upper()
while sexo not in 'FM':
    sexo = input('Dados inválidos. Digite M para Masculino ou F para Feminino: ').upper()
print('Gênero "{}" registrado com sucesso.'.format(sexo))
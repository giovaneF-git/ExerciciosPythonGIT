frase = str(input('Digite uma frase ')).strip().upper()
print('Você digitou a frase "{}"'.format(frase))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase não forma um palindromo')
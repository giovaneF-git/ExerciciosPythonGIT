num = int(input('Informe o número para descobrir se o número é primo: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número foi divisível {} vezes'.format(total))
if total == 2:
    print('sendo assim, o número é primo')
else:
    print('sendo assim, o número não é primo')
soma = 0
quantidade = 0

while quantidade < 10:
    numero = int(input('Digite um número divisível por 3: '))

    if numero % 3 == 0:
        soma += numero
        quantidade += 1
        print('Número aceito!')
    else:
        print('Número inválido! Digite um número divisível por 3.')

print(f'\nA soma dos 10 números é: {soma}')
primeiro = int(input('Digite o primeiro identificador: '))
ultimo = int(input('Digite o último identificador: '))

soma = 0
quantidade = 0

for numero in range(primeiro, ultimo + 1):
    soma += numero
    quantidade += 1

media = soma / quantidade

print(f'A média dos números no intervalo é: {media}')
soma = 0
quanti = 0

for numero in range(1, 20):
    if numero % 2 == 0 and numero > 0:
        soma += numero
        quanti += 1

media = soma / quanti

print(f'A média dos identificadores é: {media:.2f}')
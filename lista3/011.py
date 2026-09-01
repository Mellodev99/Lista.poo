valores = []

for i in range(15):
    valor = float(input(f'Digite o valor do período {i + 1}: '))
    valores.append(valor)

maior = max(valores)

print(f'O maior valor observado foi: {maior}')

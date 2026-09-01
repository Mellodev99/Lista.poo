adequados = 0
lentos = 0
soma = 0
maior = 0

for i in range(10):
    latencia = float(input(f'Digite a latência do teste {i + 1}: '))

    soma += latencia

    if latencia <= 100:
        adequados += 1
    else:
        lentos += 1

    if latencia > maior:
        maior = latencia

media = soma / 10

print('\n===== RESULTADO =====')
print(f'Testes adequados: {adequados}')
print(f'Testes lentos: {lentos}')
print(f'Média das latências: {media:.2f} ms')
print(f'Maior latência: {maior:.2f} ms')
latencias = []

for i in range(10):
    latencia = float(input(f'Digite a latência {i + 1}: '))
    latencias.append(latencia)

menor = min(latencias)

print(f'A menor latência registrada foi: {menor} ms')
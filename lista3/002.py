def calcular(a, b):
    produto = a * b

    if produto <= 1000:
        return produto
    else:
        return a + b


numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

resultado = calcular(numero1, numero2)

print(f'Resultado: {resultado}')
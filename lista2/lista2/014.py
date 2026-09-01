frase = input('digite uma frase: ')

palavras = frase.split()

contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

for palavra, quantidade in contador.items():
    print(f'{palavra}: {quantidade}')
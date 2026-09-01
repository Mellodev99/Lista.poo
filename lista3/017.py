letras = []
vogais = 0
consoantes = 0

for i in range(10):
    letra = input(f'digite a {i + 1}ª letra: ')
    letras.append(letra)

    if letra.lower() in 'aeiou':
        vogais += 1
    else:
        consoantes += 1

print('\n===== RESULTADO =====')
print(f'quantidade de vogais: {vogais}')
print(f'quantidade de consoantes: {consoantes}')
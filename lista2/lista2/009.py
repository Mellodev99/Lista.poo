notas = []
quantidade = int(input('Digite quantas notas deseja cadastrar: '))

for i in range(quantidade):
    nota = float(input('Digite suas notas: '))
    notas.append(nota)
    print(notas)
try:
    media = sum(notas) / len(notas) 
    print(f'a media das notas eh{media}')
    print(f'a maior nota eh{max(notas)}')
    print(f'a menor nota eh{min(notas)}')


except ZeroDivisionError:
    print('Não é posivel clculr  medi a list estavazia')
notas = [8, 6, 7.5, 5, 9, 4, 7, 10, 6.5, 8]
aprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1

print(f"quantidade de estudantes aprovados: {aprovados}")
alunos = {
    'Luciene': {
        'Nota 1': 8.0,
        'Nota 2': 7.5
    },
    'Buna': {
        'Nota 1': 6.0,
        'Nota 2': 7.0
    },
    'Luan': {
        'Nota 1': 9.0,
        'Nota 2': 8.0
    }
}

for aluno, notas in alunos.items():
    media = (notas['Nota 1'] + notas['Nota 2']) / 2

    if media >= 7.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    print(f'Aluno: {aluno}')
    print(f'Nota 1: {notas["Nota 1"]}')
    print(f'Nota 2: {notas["Nota 2"]}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')
  
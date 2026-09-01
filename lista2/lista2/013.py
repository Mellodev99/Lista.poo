disciplina = {
    'nome':'POO',
    'professor': 'Marao',
    'CH': '80h',
    'periodo': 3
    
}

chave = input('Digite o nome de uma chave:' )

if chave in disciplina:
    print('chave existente!')
else:
    print('chave inexistente!')    
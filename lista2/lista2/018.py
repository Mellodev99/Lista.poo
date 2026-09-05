inventario = {
    'CAT001': {
        'equipamento': 'oculos de protecao',
        'marca': 'vonder',
        'situacao': 'funcionando'
    },
    'CAT002' : {
        'equipamento': 'ferro de solda',
        'marca' : 'vonder',
        'situacao': 'em manutencao'
    },
    'CAT003': {
        'equipamento': 'multimero',
        'marca': 'vonder',
        'situacao': 'em manutencao'  #reutilizei o mesmo dicionario na lista 3
    }

}
for patrimonio, valor in inventario.items():

    print(f'\nPatrimonio: {patrimonio}')

    for chave, informacao in valor.items():
        print(f'{chave}: {informacao}')
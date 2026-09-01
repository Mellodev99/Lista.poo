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
        'situacao': 'em manutencao'
    }
}
for patrimonio, equipamento in inventario.items():
    print(f'Patrimônio: {patrimonio}')
    print(f'Equipamento: {equipamento["Equipamento"]}')
    print(f'Marca: {equipamento["Marca"]}')
    print(f'Situação: {equipamento["Situação"]}')
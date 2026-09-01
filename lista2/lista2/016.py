notas = {
    'luan': 10.0,
    'marao':9.0,
    'marcos':8.0,
    'alunox': 7.0,
    'wagner': 6.9,
    'marcio': 5.8

}

for chave, valor in notas.items():
    print(f'{chave} nota:{valor}')
    if valor >= 7:
        print('Aprovado!!')
    elif valor < 7:
        print('Reprovado')    
    

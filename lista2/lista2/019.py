notas = {

    'luan' :{
        'nota1': 9.0,
        'nota2': 8.0,       
        
    },
    'joao' :{
            'nota1': 5.0,
            'nota2': 8.8,          
            
        },
    'anderson' :{
        'nota1': 9.9,
        'nota2': 7.0, 
        
            }
}
for aluno, notas_aluno in notas.items():

    media = (notas_aluno['nota1'] + notas_aluno['nota2']) / 2
    
    print(f'\naluno: {aluno}')
    print(f'nota1: {notas_aluno['nota1']}')
    print(f'nota2: {notas_aluno['nota2']}')
    print(f'Media: {media:.2f}')

    if media >=7:
        print('Situacao:Aprovado!!')
    else:
        print('Situacao: Reprovado!')    
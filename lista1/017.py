agenda_telefonica = {}

for i in range(3):
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone: ')

    agenda_telefonica[nome] = telefone

nome_busca = input('Digite o nome que deseja procurar: ')

if nome_busca in agenda_telefonica:
    print(f'Telefone: {agenda_telefonica[nome_busca]}')
else:
    print('Contato não encontrado.')
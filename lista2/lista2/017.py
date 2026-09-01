AgendaTelefonica = {
    'marcio' : 74991675454,
    'Bruna' : 749981577825,
    'luan' : 749993645439
}

solicitacao = input('Digite um nome para obter o numero de telefone; ')

for chave, valor in AgendaTelefonica.items():
    if solicitacao == chave:
        print(valor)

  
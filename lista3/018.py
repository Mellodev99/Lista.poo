equipamentos = []

for i in range(5):
    nome = input('Digite o nom edo equipamento ')
    preco = input('Digite o preco do equipamento:')

    equipamentos.append([nome,preco ])
    print('\n===== EQUIPAMENTOS CADASTRADOS =====')

for equipamento in equipamentos:
    print(f'Nome: {equipamento[0]}')
    print(f'Preço: R$ {equipamento[1]:.2f}')
    print()

mais_caro = equipamentos[0]

for equipamento in equipamentos:
    if equipamento[1] > mais_caro[1]:
        mais_caro = equipamento

print('===== EQUIPAMENTO MAIS CARO =====')
print(f'Nome: {mais_caro[0]}')
print(f'Preço: R$ {mais_caro[1]:.2f}')
print("=========CONTROLE DE ESTOQUW:==========")

print("Digite a quantidade de produtos de cada setor:\n")
setor_A = 0
setor_B = 0
setor_C = 0
setor_D = 0

for i in range(4):
    setor = input('qual seu setor?:')

    if setor == 'A':
        setor_A = input('Digite a quantidade de produtos recebidas no seetor A: ')
        print(f'quantidade: {setor_A}')

    elif setor == 'B':
            setor_B = input('Digite a quantidade de produtos recebidas no seetor B: ')     
            print(f'quantidade: {setor_B}')
    elif setor == 'C':
            setor_C = input('Digite a quantidade de produtos recebidas no seetor C: ')
            print(f'quantidade: {setor_C}')
    elif setor == 'D':
            setor_D = input('Digite a quantidade de produtos recebidas no seetor D: ')
            print(f'quantidade: {setor_D}')     
    else:
        print("Setor inválido!\n")
print('Resumo:')
print(f'Setor A:{setor_A}| Setor B:{setor_B}| Setor C:{setor_C}| Setor D:{setor_D}|')       
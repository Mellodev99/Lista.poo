contador = 0
soma = 0
while contador < 10:
    codigo = float(input('Digite o codigo: '))

    if codigo % 6 == 0:
        print('Codigo aceito!!')
        contador += 1
        soma += codigo
    else:
        print('Codigo invalido XXX')    

print(f"A soma dos 10 números é: {codigo}")
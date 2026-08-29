financiamento = int(input('Digite o valor financiado: '))
taxa_juros = float(input('Digite a taxa de juros mensal (%): '))
meses_a_pagar = int(input('Digite a quantidade de meses a pagar: '))

juros = financiamento * (taxa_juros / 100) * meses_a_pagar
montante = financiamento + juros


print(f'Juros: R$ {juros:.2f}')
print(f'total a pagar: R$ {montante:.2f}')
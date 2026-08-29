produto = float(int('Digite o preco unitario do produto: '))
quantidade = float(int('Digite a quantidade do produto: '))
desconto = float(input('Digite o desconto a ser aplicado ao produto: '))

valor_final = (produto * quantidade) - desconto
print(f"valor finl da compra: {valor_final:.2f}")
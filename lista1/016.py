tensao = float(input("Digite a tensão (V): "))
corrente = float(input("Digite a corrente (A): "))

resistencia = tensao / corrente

print(f"Resistência elétrica: {resistencia:.2f} Ω")
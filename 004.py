import math

print('===Calculo do triangulo retângulo:===')
print('1 - Calcular a hipotenusa')
print('2 - calcular um cateto')
opcao = int(input('Escolha uma opção: '))


if opcao == 1:
    cateto1 = float(input('Digite o valor do primeiro cateto: '))
    cateto2 = float(input = ('Digite o valor do segundo cateto: '))

    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

    print(f'A hipotenusa é: {hipotenusa:.2.f}')

elif opcao == 2:
    hipotenusa = float(input("digite o valor da hipotenusa: ")) 
    cateto = float(input('digite o valor do outro cateto'))

    resultado = math.sqrt(cateto ** 2 - cateto ** 2)  

    print(f"O cateto é: {resultado:.2f}")

else:
    print("Opção inválida!") 


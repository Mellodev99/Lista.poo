L1 = int(input('Digite o primeiro valor do triangulo: '))
L2 = int(input('Digite o segundo valor do triangulo: '))
L3 = int(input('Digite o terceiro valor do triangulo: '))

if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    print('Os valores formam um triangulo!')



if L1 == L2 and L2 == L3:
    print('O triangulo é equilatero')

elif L1 != L2 and L1 != L3 and L2 != L3:
        print("O triângulo é escaleno.")


else: 
     print('os valores nao formam um triangulo')         

           
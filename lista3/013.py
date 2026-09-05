while True:
    print('\n===== CONVERSOR DE TEMPERATURA =====')
    print('1 - Celsius para Fahrenheit')
    print('2 - Fahrenheit para Celsius')
    print('3 - Celsius para Kelvin')
    print('4 - Kelvin para Celsius')
    print('5 - Fahrenheit para Kelvin')
    print('6 - Kelvin para Fahrenheit')
    print('0 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 0:
        print('Programa encerrado!')
        break

    temperatura = float(input('Digite a temperatura: '))

    if opcao == 1:
        resultado = (temperatura * 9/5) + 32
        print(f'Resultado: {resultado:.2f} °F')

    elif opcao == 2:
        resultado = (temperatura - 32) * 5/9
        print(f'Resultado: {resultado:.2f} °C')

    elif opcao == 3:
        resultado = temperatura + 273.15
        print(f'Resultado: {resultado:.2f} K')

    elif opcao == 4:
        resultado = temperatura - 273.15
        print(f'Resultado: {resultado:.2f} °C')

    elif opcao == 5:
        resultado = (temperatura - 32) * 5/9 + 273.15
        print(f'Resultado: {resultado:.2f} K')

    elif opcao == 6:
        resultado = (temperatura - 273.15) * 9/5 + 32
        print(f'Resultado: {resultado:.2f} °F')

    else:
        print('Opção inválida!')
        continue

    continuar = input('\n deseja realizar outra conversão? (s/n): ').lower()

    if continuar == 'n':
        print('programa encerrado!')
        break
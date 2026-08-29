print("=========CONTROLE DE TEMPERATURA:==========")

print("Digite a TEMPERATURA de cada SENSOR:\n")
sensor_A = 0
sensor_B = 0
sensor_C = 0


for i in range(3):
    sensor = input('qual o sensor?:')

    if sensor == 'A':
        sensor_A = float(input('Digite a temperatura resistrada  no sensor A: '))
        print(f'TEMP: {sensor_A}')
    elif sensor == 'B':
            sensor_B = float(input('Digite a tempertura registrada no sensor B: '))     
            print(f'TEMP: {sensor_B}')
    elif sensor == 'C':
            sensor_C = float(input('Digite a tempertura registrada no sensor C: '))
            print(f'TEMP: {sensor_C}')
        
    else:
        print("Sensor inválido!\n")

print('Media das temperaturas: ')    
media = (sensor_A + sensor_B + sensor_C)  / 3  
print(f'media:{media:.2f}')
print('Resumo:')
print(f'Setor A:{sensor_A}| Setor B:{sensor_B}| Setor C:{sensor_C}|')
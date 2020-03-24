base = float(input('Informe a base do triâgulo: '))
altura = float(input('Informe a altura do triâgulo: '))

while base <= 0:
    print('Informe valores positivos.')
    base = float(input('Informe a base do triâgulo: '))
    altura = float(input('Informe a altura do triâgulo: '))

while altura <= 0:
    print('Informe valores positivos.')
    base = float(input('Informe a base do triâgulo: '))
    altura = float(input('Informe a altura do triâgulo: '))

print(f'A área do triângulo é: {(base * altura) / 2}')

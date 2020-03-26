while True:

    print('Informe valores positivos.')
    base = float(input('Informe a base do triâgulo: '))
    altura = float(input('Informe a altura do triâgulo: '))

    if base and altura > 0:
        break

print(f'A área do triângulo é: {(base * altura) / 2}')


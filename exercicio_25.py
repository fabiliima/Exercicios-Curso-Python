def temperatura(celsius):
    celsius = float(input('Informe a temperatura em grau Celsius: '))
    print(f'A temperatura em F é: {celsius * (9 / 5) + 32:.2f}')


temperatura(celsius='celsius')

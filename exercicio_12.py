while True:
    num = int(input('Informe um número: '))
    if num > 0:
        print(f'O quadrado é: {num ** 2}')
        print(f'O cubo é: {num ** 3}')
        print(f'A raiz é: {num ** (1/2):.2f}')

    else:
        break

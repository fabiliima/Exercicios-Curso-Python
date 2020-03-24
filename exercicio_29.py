def triangulo_lateral(numero):
    numero = int(input('Informe um número inteiro positivo: '))
    for n in range(1, numero+1):
        print('*' * n)
    for n in range(numero-1, 0, -1):
        print('*' * n)


triangulo_lateral('numero')

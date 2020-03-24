def soma(numero):
    inicial = 0
    numero = int(input('Informe um número: '))
    for n in range(1, numero+1):
        inicial += n
    return f'A soma de 1 até {numero}: é {soma}'


print(soma('numero'))

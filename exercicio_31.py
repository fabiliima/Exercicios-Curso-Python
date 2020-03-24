def soma_algarismos(numero):
    numero = int(input('Informe um número: '))
    lista_a = [int(i) for i in str(numero)]
    print(f'A soma dos algarismos do número {numero} é {sum(lista_a)}.')


soma_algarismos('numero')

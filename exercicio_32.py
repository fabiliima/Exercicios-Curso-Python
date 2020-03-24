import random

def numeros_aleatorios():
    lista = []
    numero = int(input('Informe o número máximo para a lista: '))
    tamanho = int(input('Informe o tamanho da lista: '))
    for n in range(1, tamanho + 1):
        r = random.randint(1, numero)
        if r not in lista:
            lista.append(r)
    return lista


print(numeros_aleatorios())

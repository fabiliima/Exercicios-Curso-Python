lista_a = []
lista_b = []

for n in range(1, 11):
    n = int(input(f'Informe o número {n}/10 da primeira lista: '))
    lista_a.append(n)

for i in range(1, 11):
    i = int(input(f'Informe o número {i}/10 da segunda lista: '))
    lista_b.append(i)

ambos = set(lista_a + lista_b)
ambos_lista = list(ambos)

print(ambos_lista)

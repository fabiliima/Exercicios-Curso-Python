lista_a = []
lista_b = []
lista_c = []
lista_d = []

for n in range(1, 6):
    n = int(input(f'Informe o número {n}/5 da primeira lista (não repetir números): '))
    if n not in lista_a:
        lista_a.append(n)
    else:
        n = int(input(f'Informe um número (não repetido): '))
print(lista_a)

for a in range(1, 6):
    a = int(input(f'Informe o número {a}/5 da segunda lista (não repetir números: '))
    if a not in lista_b:
        lista_b.append(a)
    else:
        a = int(input(f'Informe um número (não repetido): '))

print(lista_b)

# 1 - Soma entre elementos na mesma posição, e em listas diferentes
for i in range(len(lista_a)):
    lista_c.append(lista_a[i] + lista_b[i])
print(lista_c)

# 2 - Multiplicação entre elementos na mesma posição, e em listas diferentes

for b in range(len(lista_a)):
    lista_d.append(lista_a[b] * lista_b[b])
print(lista_d)

# 3 - Todos elementos da lista_a que não estão na lista_b

lista_e = (set(lista_a)).difference(lista_b)
print(list(lista_e))


# 4 - Interseção - Apenas os elementos que aparecem nas duas listas

def intersection(lista_a, lista_b):
    return list(set(lista_a) & set(lista_b))


print(list(intersection(lista_a, lista_b)))

# 5 - Todos os elementos da lista A, com todos elementos da lista B que não estão em A

ambos = set(lista_a + lista_b)  
ambos_lista = list(ambos)
print(ambos_lista)


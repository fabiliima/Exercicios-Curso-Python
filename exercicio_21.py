lista_pares = []
lista_impar = []


for n in range(1, 7):
    n = int(input(f'Informe o número {n}/6: '))
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impar.append(n)


print(lista_pares)
print(f'A soma dos números pares é: {sum(lista_pares)}')

print(lista_impar)
print(f'A quantidade dos números ímpares é: {len(lista_impar)}')


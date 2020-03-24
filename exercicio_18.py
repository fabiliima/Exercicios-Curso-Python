maior = 0
menor = 1_000_000_000
soma = 0
contador = 0
total1 = 0
total2 = 0
total3 = 0
hab = int(input('Quantos habitantes há na cidade? '))
kwh = float(input('Digite o valor R$ do KWH dessa cidade: '))

for n in range(1, hab+1):
    consumo = float(input('Qual o consumo do mês deste habitante? '))
    codigo = int(input('Qual sua categoria: \n1 - Residencial \n2 - Comercial \n3 - Industrial \nDigite o código: '))

    if codigo == 1:
        total1 += consumo
    elif codigo == 2:
        total2 += consumo
    elif codigo == 3:
        total3 += consumo

    if consumo > maior:
        maior = consumo
    if consumo < menor:
        menor = consumo

    soma += consumo
    contador += 1
    media = soma / contador

print(f'O maior consumo foi de: {consumo} kwh')
print(f'O menor consumo foi de: {menor} kwh')
print(f'A média de consumo foi de {media:.2f} kwh')
print(f'O total de consumo residencial: {total1} kwh')
print(f'O total de consumo comercial: {total2} kwh')
print(f'O total de consumo industrial: {total3} kwh')

soma = 0
quant = 0
maior = -1_000_000_000
menor = 1_000_000_000
somap = 0
totalp = 0
mediap = 0
media = 0

num = float(input('Informe um número: '))

while num != 0:
    soma += num
    quant += 1
    media = soma / quant
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if num % 2 == 0:
        somap += num
        totalp += 1
        mediap = somap / totalp
    num = float(input('Informe um número: '))

print(f' A soma dos números digitados é: {soma}')
print(f'O total de números digitados é: {quant}')
print(f'A média dos números digitados é: {media:.2f}')
print(f'O maior número digitado é: {maior}')
print(f'O menor número digitado é: {menor}')
print(f'A média dos números pares é: {mediap:.2f}')

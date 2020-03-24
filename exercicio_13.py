soma = 0
contador = 0

while True:
    idade = int(input('Informe a idade: '))
    if idade > 0:
        soma += idade
        contador += 1
    else:
        break
print(f'A média das idades é: {soma / contador}')

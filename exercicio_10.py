altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))

imc = peso / (altura ** 2)

if imc <= 18.50:
    print(f'IMC: {imc:.2f}: Abaixo do peso')
elif imc >= 18.60 and imc <= 24.99:
    print(f'IMC: {imc:.2f}: Saudável')
elif imc >= 25 and imc <= 29.99:
    print(f'IMC: {imc:.2f}: Peso em excesso')
elif imc >= 30 and imc <= 34.99:
    print(f'IMC: {imc:.2f}: Obesidade Grau I')
elif imc >= 35 and imc <= 39.99:
    print(f'IMC: {imc:.2f}: Obesidade Grau II (Severa)')
elif imc >= 40:
    print(f'IMC: {imc:.2f}: Obesidade Graus III (Mórbida)')

altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
grau_imc = ''
imc = peso / (altura ** 2)

if imc >= 40:
    grau_imc = 'Obesidade Graus III (Mórbida)'

elif imc >= 35 and imc <= 39.99:
    grau_imc = 'Obesidade Grau II (Severa)'

elif imc >= 30 and imc <= 34.99:
    grau_imc = 'Obesidade Grau I'

elif imc >= 25 and imc <= 29.99:
    grau_imc = 'Peso em excesso'

elif imc >= 18.60 and imc <= 24.99:
    grau_imc = 'Saudável'

else:
    grau_imc = 'Abaixo do peso'

print(f'IMC: {imc:.2f} Grau IMC: {grau_imc}')

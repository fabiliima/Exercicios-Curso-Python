valor_1 = float(input('Qual o valor do maior salário? '))  # o segundo salário é um terço deste valor
valor_2 = float(valor_1 / 3)
inv_poupanca = valor_1 * 1.2
inv_caderneta = valor_2 * 1.5
meses = 0

while inv_caderneta < inv_poupanca:
    inv_poupanca += inv_poupanca * 0.2
    inv_caderneta += inv_caderneta * 0.5
    meses += 1
if inv_caderneta >= inv_poupanca:
    print(f'O valor do investimento na poupança é: {inv_poupanca:.2f} ')
    print(f'O valor do investimento na caderneta é: {inv_caderneta:.2f} ')
    print(f'Demorou {meses} meses para alcançar este valor.')

salario = float(input('Informe seu salário atual: '))
tempo = int(input('Quantos anos você trabalha nesta empresa? '))

if salario <= 500:
    salario_reajuste = salario * 1.25
    if tempo < 1:
        bonus = 0
        print('Funcionário não tem direito ao bônus')
    if tempo >= 1  and tempo <= 3:
        bonus = 100
    if tempo >= 4 and tempo <= 6:
        bonus = 200
    if tempo >= 7 and tempo <= 10:
        bonus = 300
    if tempo > 10:
        bonus = 500
    print(f'O novo salário (bônus + reajuste) é: R$ {salario_reajuste + bonus:.2f}')

elif salario <= 1000:
    salario_reajuste = salario * 1.20
    if tempo < 1:
        bonus = 0
        print('Funcionário não tem direito ao bônus')
    if tempo >= 1  and tempo <= 3:
        bonus = 100
    if tempo >= 4 and tempo <= 6:
        bonus = 200
    if tempo >= 7 and tempo <= 10:
        bonus = 300
    if tempo > 10:
        bonus = 500
    print(f'O novo salário (bônus + reajuste) é: R$ {salario_reajuste + bonus:.2f}')

elif salario <= 1500:
    salario_reajuste = salario * 1.15
    if tempo < 1:
        bonus = 0
        print('Funcionário não tem direito ao bônus')
    if tempo >= 1  and tempo <= 3:
        bonus = 100
    if tempo >= 4 and tempo <= 6:
        bonus = 200
    if tempo >= 7 and tempo <= 10:
        bonus = 300
    if tempo > 10:
        bonus = 500
    print(f"O novo salário (bônus + reajuste) é: R$ {salario_reajuste + bonus:.2f}")

elif salario <= 2000:
    salario_reajuste = salario * 1.10
    if tempo < 1:
        bonus = 0
        print('Funcionário não tem direito ao bônus')
    if tempo >= 1  and tempo <= 3:
        bonus = 100
    if tempo >= 4 and tempo <= 6:
        bonus = 200
    if tempo >= 7 and tempo <= 10:
        bonus = 300
    if tempo > 10:
        bonus = 500
    print(f'O novo salário (bônus + reajuste) é: R$ {salario_reajuste + bonus:.2f}')

elif salario > 2000:
    salario_reajuste = salario
    print('Funcionário não tem direito a reajuste.')
    if tempo < 1:
        bonus = 0
        print('Funcionário não tem direito ao bônus')
    if tempo >= 1  and tempo <= 3:
        bonus = 100
    if tempo >= 4 and tempo <= 6:
        bonus = 200
    if tempo >= 7 and tempo <= 10:
        bonus = 300
    if tempo > 10:
        bonus = 500
    print(f'O novo salário (bônus + reajuste) é: R$ {salario_reajuste + bonus:.2f}')

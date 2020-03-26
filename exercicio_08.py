bonus = 0
salario_reajuste = 0

salario = float(input('Informe seu salário atual: '))
tempo = int(input('Quantos anos você trabalha nesta empresa? '))

if tempo > 10:
    bonus = 500

elif tempo >= 7 and tempo <= 10:
    bonus = 300

elif tempo >= 4 and tempo <= 6:
    bonus = 200

elif tempo >= 1 and tempo <= 3:
    bonus = 100

else:
    print('Funcionário não tem direito ao bônus.')

if salario > 2000:
    salario_reajuste = salario
    print('Funcionário não tem direito a reajuste de salário.')

elif salario <= 2000:
    salario_reajuste = salario * 1.10

elif salario <= 1500:
    salario_reajuste = salario * 1.15

elif salario <= 1000:
    salario_reajuste = salario * 1.20

elif salario <= 500:
    salario_reajuste = salario * 1.25

print(f'O novo salário (se aplicável bônus + reajuste) é: R$ {salario_reajuste + bonus:.2f}')

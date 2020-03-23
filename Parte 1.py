# Exercicios-Curso-Python PT1

# Faça um programa que leia 2 notas, verifica-se as notas são válidas e imprime a média, uma nota válida, é um valor entre 0 e 10, caso contrário informar erro ao usuário e finalizar o programa.
nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

if nota_1 and nota_2 > 0 < 10:
    print(f'A média é: {(nota_1 + nota_2) / 2:.2f}')
else:
    print('A nota deve ser entre 0 e 10.')]

# Faça um programa que leia um inteiro entre 1 e 7, e imprima o dia da semana correspondente a este número.Isto é 1 = domingo, 2 = segunda-feira e assim por diante.

dia_da_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
dia = int(input('Informe um número de 1 á 7: '))

if dia >= 1 and dia <=7:
    print(f' Hoje é {dia_da_semana[dia - 1]}.')  
else:
    print('Número inválido.')
    
# Faça um programa que leia um número inteiro entre 1 e 12, e imprima o mês correspondente a este número.Isto é 1 = janeiro, 2 = fevereiro e assim por diante.

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro',
       # 11
       'dezembro')
mes = int(input('Informe um número de 1 á 12: '))

if mes >= 1 and mes <= 12:
    print(
        f' Este mês é {meses[mes - 1]}.')  
else:
    print('Número inválido.')
 
 # Faça um programa que leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As regras são:
 # Ter pelo menos 65 anos;
 # Ou ter trabalhado no mínimo 30 anos;
 # Ou ter pelo menos 60 anos e trabalhado no mínimo 25 anos;
 
 idade = int(input('Qual sua idade? '))
tempo_trabalho = int(input('Quantos anos você trabalhou? '))

if idade >= 65:
    print('Você pode aposentar!')
elif tempo_trabalho >= 30:
    print('Você pode aposentar!')
elif idade >= 60 and tempo_trabalho >= 25:
    print('Você pode aposentar!')
else:
    print('Você não pode aposentar!')
 
# Faça um programa que determine se um ano é bissexto ou não. Um ano é bissexto se for divisível por 400 ou por 4 e não for divisível por 100.

ano = int(input('Informe o ano: '))

if ano % 400 == 0:
    print('Ano bissexto!')
elif ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto!')
else:
    print('Ano não bissexto!')
  
 # Faça um programa que dado a idade de um nadador, classifique-o em categorias.
 
idade = int(input('Informe a idade: '))

if idade >= 5 and idade <=7:
    print('Infantil A')
elif idade >= 8 and idade <= 10:
    print('Infantil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Sênior')
else:
    print('Idade incompatível com a natação.')
 
 # Um produto vai sofrer aumento de preço. Leia o preço antigo, calcule e escreva o preço novo e escreva uma mensagem em função do preço novo.
 
preco_novo = 0
preco_antigo = float(input('Informe o preço antigo do produto: R$ '))

if preco_antigo < 50:
    preco_novo = preco_antigo * 1.05
elif preco_antigo >= 50 and preco_antigo <= 100:
    preco_novo = preco_antigo * 1.10
elif preco_antigo > 100:
    preco_novo = preco_antigo * 1.15

if preco_novo < 80:
    print(f'{preco_novo:.2f}')
    print('Barato')
elif preco_novo >= 80 and preco_novo <= 120:
    print(f'{preco_novo:.2f}')
    print('Normal')
elif preco_novo > 120 and preco_novo <= 200:
    print(f'{preco_novo:.2f}')
    print('Caro')
elif preco_novo > 200:
    print(f'{preco_novo:.2f}')
    print('Muito Caro')
 
# Uma empresa decide dar aumento ao seus funcionários, considerando o salário atual e o tempo de serviço. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com salário maior e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salario. Faça um programa que leia: o salário atual e os anos que este funcionário trabalha na empresa. Calcule o salário reajustado ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

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

# O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica. Leia o custo de fábrica e escreva o custo ao consumidor.

custo_fabrica = float(input('Qual o custo de fábrica do carro? '))

if custo_fabrica < 12_000:
    comissao_distribuidor = custo_fabrica * 0.05
    impostos = 0
    print(f'O custo para o consumidor é: R$ {custo_fabrica + comissao_distribuidor + impostos:.2f}')
    
if custo_fabrica > 12_000 and custo_fabrica <= 25_000:
    comissao_distribuidor = custo_fabrica * 0.10
    impostos = custo_fabrica * 0.15
    print(f'O custo para o consumidor é: R$ {custo_fabrica + comissao_distribuidor + impostos:.2f}')
    
if custo_fabrica > 25_000:
    comissao_distribuidor = custo_fabrica * 0.15
    impostos = custo_fabrica * 0.20
    print(f'O custo para o consumidor é: R$ {custo_fabrica + comissao_distribuidor + impostos:.2f}')


# Faça um programa que calcule o IMC e mostre sua classificação.

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

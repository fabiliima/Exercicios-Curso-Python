idade = int(input('Qual sua idade? '))
tempo_trabalho = int(input('Quantos anos você trabalhou? '))

if idade >= 65 or tempo_trabalho >= 30 or idade >= 60 and tempo_trabalho >= 25:
    print('Você pode aposentar!')
else:
    print('Você não pode aposentar!')


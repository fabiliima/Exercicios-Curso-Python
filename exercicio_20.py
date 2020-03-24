altura_alunos = {}

for n in range(1, 11):
    n = int(input('Informe o código deste aluno: '))
    altura_alunos[n] = float(input(f'Informe a altura do aluno (código {n}): '))

maximo = max(altura_alunos.values())
minimo = min(altura_alunos.values())
chave_maximo = []
chave_minimo = []

for key, values in altura_alunos.items():
    if values == maximo:
        chave_maximo.append(key)
print(f'A maior altura é: {maximo} e o código(s) do aluno(s): {chave_maximo}')

for key, values in altura_alunos.items():
    if values == minimo:
        chave_minimo.append(key)
print(f'A menor altura é: {minimo} e o código(s) do aluno(s): {chave_minimo}')

print(altura_alunos)

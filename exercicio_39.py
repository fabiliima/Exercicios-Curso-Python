cidade_habitantes = {}

while True:
    n = input('Informe o nome da cidade ou digite 0 para sair: ').title()
    if n == '0':
        break
    cidade_habitantes[n] = float(input(f'Informe a quantidade de habitantes ({n}): '))

with open('arq.txt', 'w', encoding='utf-8') as arquivo1:
    arquivo1.write(str(cidade_habitantes))

maximo = max(cidade_habitantes.items(), key=lambda k: k[1])  # pega chave e valor máximo

with open('arq2.txt', 'w', encoding='utf-8') as arquivo2:
    arquivo2.write(str(maximo))

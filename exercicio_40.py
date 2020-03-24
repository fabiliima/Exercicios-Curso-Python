usuario_telefone = {}

while True:
    n = input('Informe o nome do usuário ou digite 0 para sair: ').title()
    if n == '0':
        break
    usuario_telefone[n] = (input(f'Informe o número de telefone deste usuário ({n}): '))

with open('arq.txt', 'w', encoding='utf-8') as arquivo1:
    arquivo1.write(str(usuario_telefone))

with open('arq.txt', encoding='utf-8') as arquivo1:
    print(arquivo1.read())

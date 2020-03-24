with open('arq.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        texto = input('Informe um conteúdo para o arquivo ou digite 0 para sair: ')
        if texto != '0':
            arquivo.write(texto + '\n')
        else:
            break

with open('arq.txt') as arquivo:
    with open('arq2.txt', 'w', encoding='utf-8') as arquivo2:
        for line in arquivo.readlines():
            arquivo2.write(line)

with open('arq2.txt', 'r', encoding='utf-8') as arquivo2:
    string = arquivo2.read().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')

with open('arq2.txt', 'w', encoding='utf-8') as arquivo2:
    arquivo2.write(string)

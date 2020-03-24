with open('arq.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        texto = input('Informe um conteúdo para o arquivo ou digite 0 para sair: ')
        if texto != '0':
            arquivo.write(texto + '\n')
        else:
            break

with open('arq.txt') as arquivo:
    vogais = [letra for letra in arquivo.read() if letra.lower() in ['a', 'e', 'i', 'o', 'u']]
    print(f'O número de vogais no arquivo é: {len(vogais)}')

with open('arq.txt') as arquivo:
    consoantes = [letra for letra in arquivo.read() if letra.lower() in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                                                                         'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x',
                                                                         'w', 'x', 'y', 'z']]
    print(f'O número de consoantes no arquivo é: {len(consoantes)}')
